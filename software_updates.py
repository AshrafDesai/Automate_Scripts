##Develop a script to check for available software updates on the system.
##FOR Windows
import win32com.client

def check_for_updates():
    try:
        
        update_session = win32com.client.Dispatch('Microsoft.Update.Session')

        
        update_searcher = update_session.CreateUpdateSearcher()

        print("Searching for available updates...")

        
        search_result = update_searcher.Search("IsInstalled=0")

        
        if search_result.Updates.Count > 0:
            print(f"Found {search_result.Updates.Count} update(s) available:")
            for update in search_result.Updates:
                print(update.Title)
            
           
            user_input = input("Do you want to install these updates? (yes/no): ").lower()
            if user_input == 'yes':
                install_updates(search_result)
            else:
                print("Updates will not be installed.")
        else:
            print("No updates available.")

    except Exception as e:
        print(f"An error occurred: {e}")

def install_updates(search_result):
    try:
        
        update_collection = win32com.client.Dispatch("Microsoft.Update.UpdateColl")

        
        for update in search_result.Updates:
            update_collection.Add(update)

        
        update_installer = win32com.client.Dispatch("Microsoft.Update.Installer")

        
        installation_result = update_installer.Install(update_collection)

        
        if installation_result.ResultCode == 2:
            print("Updates installed successfully.")
        else:
            print("Failed to install updates.")

    except Exception as e:
        print(f"An error occurred during installation: {e}")

if __name__ == "__main__":
    check_for_updates()
