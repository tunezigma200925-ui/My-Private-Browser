import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage

# A Private Browser made in Python
class PrivateBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Private Browser")
        self.resize(1200, 800)
        
        # Setup Browser Engine
        self.browser = QWebEngineView()
        
        # --- PRIVACY LOGIC ---
        # "MemoryHttpCache" means data is stored in RAM, not Hard Drive.
        # "NoPersistentCookies" means cookies are deleted when closed.
        self.profile = QWebEngineProfile("PrivateProfile", self.browser)
        self.profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        
        page = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(page)
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
        
        self.setCentralWidget(self.browser)
        
        # Setup Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        # Back Button
        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        # Reload Button
        reload_btn = QAction('Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        # Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrivateBrowser()
    window.show()
    sys.exit(app.exec_())
