import os, Blender

try:
    nifDataPath = Blender.sys.sep.join((os.getenv("ProgramFiles"), "Bethesda", "Oblivion", "Data", ""))
except TypeError:
    nifDataPath = ''

# This "module" holds all the fallback values for the script configuration. This
# makes sure the configuration will never be invalid
_CFG_NIF_IMPORT_PATH = "%sMeshes" % (nifDataPath)
# The 'r' before the string definition sets this as "raw". This means that escape
# sequences (those preceded by '\' won't be interpreted. Handy to set paths in
# Win32, and let's face it, almost all the script users will be Win32 users.
_CFG_NIF_EXPORT_PATH = "%sMeshes" % (nifDataPath)
# These next two are selected in the import and export screens, not in the config
_CFG_NIF_IMPORT_FILE = ""
_CFG_NIF_EXPORT_FILE = "export.nif"
_CFG_REALIGN_BONES = True
_CFG_IMPORT_ANIMATION = True
_CFG_IMPORT_SCALE_CORRECTION = 0.1
_CFG_EXPORT_SCALE_CORRECTION = 1.0 / _CFG_IMPORT_SCALE_CORRECTION
_CFG_BASE_TEXTURE_FOLDER = "%sTextures" % (nifDataPath)
_CFG_TEXTURE_SEARCH_PATH = [_CFG_BASE_TEXTURE_FOLDER]
_CFG_EXPORT_VERSION = '20.0.0.5'
_CFG_EXPORT_TEXTURE_PATH = "R"
# (R)elative to NIF,
# (F)ull,
# (N)one (strip folders),
# Relative to (B)ase texture folder

# the following items are used for dtermining internal
_CFG_EPSILON = 0.005 # used for checking equality with floats
_CFG_VERBOSITY = 3 # verbosity level, determines how much debug output will be generated



