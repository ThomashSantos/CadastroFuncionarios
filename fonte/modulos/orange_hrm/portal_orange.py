from playwright.sync_api import Playwright
from fonte import logging
import os


class PortalOrangeHRM:
    def __init__(self, playwright: Playwright):
        self._user = os.environ.get("ORANGE_HRM_USER")
        self._password = os.environ.get("ORANGE_HRM_PASSWORD")
        self._browser = playwright.chromium.launch(channel="chrome", headless=False, slow_mo=1000)
        self._context = self._browser.new_context(base_url=os.environ.get("ORANGE_HRM_URL"))
        self._page = self._context.new_page()
        self._page.set_viewport_size({"width": 1920, "height": 1080})

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._context.close()
        self._browser.close()

    def login(self):
        self._page.goto("web/index.php/auth/login")
        self._page.get_by_role("textbox", name="Username").fill(self._user)
        self._page.get_by_role("textbox", name="Password").fill(self._password)
        self._page.get_by_role("button", name="Login").click()
        logging.info("Login realizado com sucesso no OrangeHRM.")

    def cadastra_candidato(self, dados_candidato: dict, resume_candidato: str):
        self._page.goto("web/index.php/recruitment/addCandidate")
        self._page.get_by_role("textbox", name="First Name").fill(dados_candidato.get("first_name", ""))
        self._page.get_by_role("textbox", name="Middle Name").fill(dados_candidato.get("middle_name", ""))
        self._page.get_by_role("textbox", name="Last Name").fill(dados_candidato.get("last_name", ""))
        self._page.locator("form i").first.click()
        self._page.locator(f"//span[text()='{dados_candidato.get('vacancy')}']").click()
        self._page.locator("//label[text()='Email']//following::input").first.fill(dados_candidato.get("email", ""))
        self._page.locator("//label[text()='Contact Number']//following::input").first.fill(dados_candidato.get("contact_number", ""))
        self._page.locator("//input[@type='file']").set_input_files(resume_candidato)
        keywords = ','.join(dados_candidato.get('keywords').split('; '))
        self._page.locator("//label[text()='Keywords']//following::input").first.fill(keywords)
        self._page.get_by_role("button", name="Save").click()
        self._page.get_by_role("button", name="Shortlist").wait_for(timeout=100000, state='visible')
        logging.info(f"Candidato: {dados_candidato.get('full_name')} cadastrado com sucesso no OrangeHRM.")

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        with PortalOrangeHRM(playwright) as portal:
            portal.login()
            portal.cadastra_candidato({'full_name': 'Ana Beatriz Souza', 'vacancy': 'Senior QA Lead', 'email': 'ana.beatriz.souza@email.com', 'contact_number': '(11) 98765-4321', 'keywords': 'Empatia; Liderança; Comunicação', 'first_name': 'Ana', 'middle_name': 'Beatriz', 'last_name': 'Souza'},
                                      resume_candidato="/Users/thomas/Documentos/Python/Code/Entrevista/Botcity/CadastroFuncionarios/fonte/dados/saida/resume_ana.txt")