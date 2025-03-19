from pywebcopy import save_website

url = 'https://golde.co'
download_folder = 'F:/downloads'

save_website(
    url=url,
    project_folder=download_folder,
    bypass_robots=True,
    debug=True,
    open_in_browser=False,
    delay=None,
    threaded=False,
)

print("Website has been successfully downloaded.")
