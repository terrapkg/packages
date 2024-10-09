# Improved interactions between the Steam runtime and host distribution
# libraries, which should let Steam work out of the box with open-source
# graphics drivers on modern distributions. If using an older distribution or
# running into problems, set variable at 0 to revert to the previous behavior.
# export STEAM_RUNTIME_PREFER_HOST_LIBRARIES=0

# Unify close-to-tray behavior with other platforms. If using a distribution
# that doesn't have proper compatible tray support set variable at 0.
export STEAM_FRAME_FORCE_CLOSE=1

# Do not minimize main Steam window after losing focus (i.e. exiting a game in
# Steam Remote Play.
# https://github.com/ValveSoftware/steam-for-linux/issues/4611
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0
