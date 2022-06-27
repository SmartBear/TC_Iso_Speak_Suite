def Mod_Close_TestedApp():
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Mod_Close_TestedApp")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Close_TestedApp", "This is a module template to be used as a seed for new modules", pmNormal, Project.Variables.LogAtrribModTitle)
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

def Mod_Start_TestedApp():
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Mod_Start_TestedApp")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Start_TestedApp", "This is a module template to be used as a seed for new modules", pmNormal, Project.Variables.LogAtrribModTitle)
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run(1, True)
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()
