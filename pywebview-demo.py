from flask import Flask
import webview


def main():
    app = Flask("PyWebView-Demo")
    
    @app.route('/')
    def index():
        return "<h1>PyWebView-Demo</h1>\n<p>Hello from Flask</p>"

    window = webview.create_window("PyWebView-Demo", app)
    webview.start()


if __name__=="__main__":
    main()

