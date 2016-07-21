import swat_settings
from assembla import API


class GlobalInfo(object):
    def __init__(self):
        self.assembla = None
        self.swat_space = None
        self.swat_users = None
        self.seismic_tickets = None

    def load(self):
        self.assembla = API(key=swat_settings.SWAT_API_KEY, secret=swat_settings.SWAT_API_SECRET)
        self.swat_space = self.assembla.spaces(name=swat_settings.SWAT_SPACE_NAME)[0]
        self.swat_users = self.__get_swat_user_info()
        self.seismic_tickets = self.swat_space.tickets()

    def __get_swat_user_info(self):
        swat_users = []
        for user in self.swat_space.users():
            if 'email' in user.keys() and user['email'] in swat_settings.SWAT_EMAILS:
                swat_users.append(user)

        return swat_users


GLOBAL_INFO = GlobalInfo()
