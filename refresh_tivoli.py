
import tableauserverclient as TSC
f=open("account.txt","r")
lines=f.readlines()
token=lines[1].strip()
site_id=lines[4].strip()
server_url=lines[7].strip()
workbook_id=lines[10].strip()
token_name=lines[13].strip()
f.close()
tableau_auth = TSC.PersonalAccessTokenAuth(token_name, token, '')
server = TSC.Server(server_url, use_server_version=True)

with server.auth.sign_in(tableau_auth):

    # get the workbook item from the site
    workbook = server.workbooks.get_by_id(workbook_id)

    # call the update method
    workbook = server.workbooks.refresh(workbook)
    print("\nThe data of workbook {0} is refreshed.".format(workbook.name))