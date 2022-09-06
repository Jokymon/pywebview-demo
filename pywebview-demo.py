from flask import Flask
import webview


def main():
    app = Flask("PyWebView-Demo", static_folder="gui")
    
    @app.route('/')
    def index():
        return app.send_static_file("index.html")

    window = webview.create_window("PyWebView-Demo", app)
    webview.start(debug=True)


if __name__=="__main__":
    main()

