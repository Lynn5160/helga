
"""
asset_manager_button
==========================================

Subclass of QPushButton to allow for customized drag&drop behaviour
"""












#Import
#------------------------------------------------------------------
#python
import os
import logging
#PySide
from PySide import QtGui
from PySide import QtCore




#Import variable
do_reload = True


#asset_manager

#asset_manager_globals
from lib import asset_manager_globals
if(do_reload):reload(asset_manager_globals)






#Globals
#------------------------------------------------------------------

#Pathes
TOOL_ROOT_PATH = asset_manager_globals.TOOL_ROOT_PATH
MEDIA_PATH = asset_manager_globals.MEDIA_PATH
ICONS_PATH = asset_manager_globals.ICONS_PATH

#AssetManager colors
BRIGHT_ORANGE = asset_manager_globals.BRIGHT_ORANGE
DARK_ORANGE = asset_manager_globals.DARK_ORANGE
BRIGHT_GREY = asset_manager_globals.BRIGHT_GREY
GREY = asset_manager_globals.GREY
DARK_GREY = asset_manager_globals.DARK_GREY









#AssetManagerButton class
#------------------------------------------------------------------
class AssetManagerButton(QtGui.QPushButton):
    """
    Subclass of QPushButton to allow for custom styling
    """

    def __new__(cls, *args, **kwargs):
        """
        AssetManagerButton instance factory.
        """

        #asset_manager_button_instance
        asset_manager_button_instance = super(AssetManagerButton, cls).__new__(cls, args, kwargs)

        return asset_manager_button_instance

    
    def __init__(self, 
                logging_level = logging.DEBUG,
                button_text = None,
                icon_name = None,
                fixed_width = None,
                fixed_height = None,
                background_color_normal = DARK_GREY,
                hover_radial_color_normal = DARK_ORANGE,
                background_color_active = GREY,
                hover_radial_color_active = DARK_ORANGE,
                hover_radial_radius = 0.45,
                label_header_text = 'label_header_text',
                label_text = 'label_text',
                metadata_color_normal = GREY,
                metadata_color_active = QtGui.QColor(255, 0, 0),
                parent=None):
        """
        AssetManagerButton instance customization.
        """

        #parent_class
        self.parent_class = super(AssetManagerButton, self)
        
        #super class constructor
        if(button_text):
            self.parent_class.__init__(button_text, parent)
        else:
            self.parent_class.__init__(parent)


        #instance variables
        #------------------------------------------------------------------
        self.button_text = button_text
        self.icon_name = icon_name
        self.fixed_width = fixed_width
        self.fixed_height = fixed_height
        
        #colors
        self.background_color_normal = background_color_normal
        self.hover_radial_color_normal = hover_radial_color_normal
        self.background_color_active = background_color_active
        self.hover_radial_color_active = hover_radial_color_active

        #hover_radial_radius
        self.hover_radial_radius = hover_radial_radius

        #icon_path
        self.icon_path = os.path.join(ICONS_PATH, self.icon_name)
        self.icon_path = self.icon_path.replace('\\', '/')

        #label_header_text
        self.label_header_text = label_header_text
        #label_text
        self.label_text = label_text

        #metadata_color_normal
        self.metadata_color_normal = metadata_color_normal
        #metadata_color_active
        self.metadata_color_active = metadata_color_active

        
        
        

        
        #logger
        #------------------------------------------------------------------
        #logger
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logging_level = logging_level
        self.logger.setLevel(self.logging_level)


        #Init procedure
        #------------------------------------------------------------------

        #setup_additional_ui
        self.setup_additional_ui()

        #connect_ui
        self.connect_ui()









    #UI setup methods
    #------------------------------------------------------------------
    
    def setup_additional_ui(self):
        """
        Setup additional UI.
        """
        
        #setMouseTracking
        self.setMouseTracking(True)

        #set_size_policy
        self.set_size_policy(self.fixed_width, self.fixed_height)

        #initialize_icons
        #self.initialize_icons()

        #set_stylesheet
        self.set_stylesheet()


    def connect_ui(self):
        """
        Connect UI widgets with slots or functions.
        """
        
        pass




    


    #Slots
    #------------------------------------------------------------------

    def set_stylesheet(self, role = 'normal'):
        """
        Set stylesheet for this widget based on role.
        """

        #log
        self.logger.debug('Set stylesheet for role: {0}'.format(role))

        #stylesheet_str
        stylesheet_str = self.get_stylesheet(role)
        #set stylesheet
        self.setStyleSheet(stylesheet_str)


    def get_stylesheet(self, role = 'normal'):
        """
        Get stylesheet for a certain role.
        """

        #normal
        if (role == 'normal'):
            return self.get_stylesheet_normal()

        #active
        elif (role == 'active'):
            return self.get_stylesheet_active()
            

    def get_stylesheet_normal(self):
        """
        Get stylesheet for role "normal".
        """

        #ss_dict
        ss_dict = {'icon_path' : self.icon_path,
                    'hover_radial_radius' : self.hover_radial_radius,
                    'background_color_normal' : self.background_color_normal.name(),
                    'hover_radial_color_normal' : self.hover_radial_color_normal.name(),
                    'background_color_active' : self.background_color_active.name(),
                    'hover_radial_color_active' : self.hover_radial_color_active.name(),}
        
        #ss_normal
        ss_normal = " \
\
\
/* AssetManagerButton - normal */\
AssetManagerButton { border-image: url(%(icon_path)s); \
                        background-color: %(background_color_normal)s; \
} \
\
\
/* AssetManagerButton - normal - hover */\
AssetManagerButton:hover { border-image: url(%(icon_path)s); \
                            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, \
                                                                radius:%(hover_radial_radius)s, fx:0.5, fy:0.5, \
                                                                stop:0 %(hover_radial_color_normal)s, \
                                                                stop:1 %(background_color_normal)s); \
} \
\
\
/* AssetManagerButton - normal - pressed */\
AssetManagerButton:pressed { border-image: url(%(icon_path)s); \
                                background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, \
                                                                    radius:%(hover_radial_radius)s, fx:0.5, fy:0.5, \
                                                                    stop:0 %(hover_radial_color_normal)s, \
                                                                    stop:1 %(background_color_normal)s); \
} \
\
\
"%ss_dict
        
        #return
        return ss_normal


    def get_stylesheet_active(self):
        """
        Get stylesheet for role "active".
        """

        #ss_dict
        ss_dict = {'icon_path' : self.icon_path,
                    'hover_radial_radius' : self.hover_radial_radius,
                    'background_color_normal' : self.background_color_normal.name(),
                    'hover_radial_color_normal' : self.hover_radial_color_normal.name(),
                    'background_color_active' : self.background_color_active.name(),
                    'hover_radial_color_active' : self.hover_radial_color_active.name(),}

        #ss_active
        ss_active = " \
\
\
/* AssetManagerButton - active */\
AssetManagerButton { border-image: url(%(icon_path)s); \
                        background-color: %(background_color_active)s; \
} \
\
\
/* AssetManagerButton - active - hover */\
AssetManagerButton:hover { border-image: url(%(icon_path)s); \
                            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, \
                                                                radius:%(hover_radial_radius)s, fx:0.5, fy:0.5, \
                                                                stop:0 %(hover_radial_color_active)s, \
                                                                stop:1 %(background_color_active)s); \
} \
\
\
/* AssetManagerButton - active - pressed */\
AssetManagerButton:pressed { border-image: url(%(icon_path)s); \
                                background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, \
                                                                    radius:%(hover_radial_radius)s, fx:0.5, fy:0.5, \
                                                                    stop:0 %(hover_radial_color_active)s, \
                                                                    stop:1 %(background_color_active)s); \
} \
\
\
"%ss_dict

        #return
        return ss_active








    


    #Getter & Setter
    #------------------------------------------------------------------

    def set_background_color_normal(self, color):
        """
        Set self.background_color_normal
        """
        
        self.background_color_normal = color


    def set_background_color_active(self, color):
        """
        Set self.background_color_active
        """
        
        self.background_color_active = color


    def set_hover_radial_color_normal(self, color):
        """
        Set self.hover_radial_color_normal
        """
        
        self.hover_radial_color_normal = color


    def set_hover_radial_color_active(self, color):
        """
        Set self.hover_radial_color_active
        """
        
        self.hover_radial_color_active = color










    

    #Methods
    #------------------------------------------------------------------

    def initialize_icons(self, resize_factor = 0.5):
        """
        Create and scale self.icon and self.icon_hover
        """

        #icon_width
        icon_width = int(self.width() * resize_factor)
        #icon_height
        icon_height = int(self.height() * resize_factor)

        #icon
        self.pixmap_icon = QtGui.QPixmap(os.path.join(ICONS_PATH, self.icon_name))
        self.pixmap_icon = self.pixmap_icon.scaled(icon_width, icon_height, mode = QtCore.Qt.FastTransformation)
        self.icon = QtGui.QIcon(self.pixmap_icon)

        #log
        self.logger.debug('Initialized icon {0} for button {1}'.format(self.icon_name, self))

        #setIcon
        self.setIcon(self.icon)


    def set_size_policy(self, width, height):
        """
        Set size policy for self.
        """

        #fixed width and height
        if (width and height):
            self.setFixedSize(width, height)

        #else
        else:

            #set expanding
            expanding_size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
            self.setSizePolicy(expanding_size_policy)

            #fixed width
            if(width):
                self.setFixedWidth(width)

            #fixed height
            elif(height):
                self.setFixedHeight(height)
