import znc

class checkmod(znc.Module):
    module_types = [znc.CModInfo.GlobalModule]
    description = "Checks that a module is loaded for a user"

    def CheckUserModule(self, module):
        users = znc.CZNC.Get().GetUserMap()
        for user in users.items():

            loaded_user_mods = []
            for mod in user[1].GetModules():
                loaded_user_mods.append(mod.GetModName())

            if module not in loaded_user_mods:
                self.PutModule("LoadModule " + user[0] + " " + module)

    def CheckNetworkModule(self, module, network):
        users = znc.CZNC.Get().GetUserMap()
        for user in users.items():

            net = user[1].FindNetwork(network)

            if net:
                loaded_net_mods = []
                for mod in net.GetModules():
                    loaded_net_mods.append(mod.GetModName())

                if module not in loaded_net_mods:
                    self.PutModule("LoadNetModule " + user[0] + " " + network + " " + module)
            else:
                self.PutModule(user[0] + " network " + network +  " not found")

    def OnModCommand(self, command):
            if command.split()[0] == "checkusermod":
                self.CheckUserModule(command.split()[1])
            elif command.split()[0] == "checknetmod":
                self.CheckNetworkModule(command.split()[1], command.split()[2])