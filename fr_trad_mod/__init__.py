from modloader.modclass import Mod, loadable_mod


@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("FR Translation", "1.0", "BananaSplit")

    def mod_load(self):
        pass

    def mod_complete(self):
        pass