import winreg

# function to get the current theme
def get_current_theme():
    # open the registry key to get the current theme
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
    # get the value of the key and return it
    value = winreg.QueryValueEx(key, "AppsUseLightTheme")
    return "light" if value[0] == 1 else "dark"

print(get_current_theme())
