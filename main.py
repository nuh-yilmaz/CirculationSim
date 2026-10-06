import os
import sys
import webview

def get_asset_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller single-file bundle """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    content_dir = get_asset_path('html_content')
    entry_point = os.path.join(content_dir, 'index.html')

    # Create full-featured native window
    window = webview.create_window(
        title='Circulation Simulation Suite',
        url=entry_point,
        width=1400,
        height=900,
        resizable=True
    )
    
    # Enables local HTTP server so assets like Pulse.png work seamlessly
    webview.start(http_server=True)
