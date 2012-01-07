# -----------------------------------------------------------------------------
# ROS settings
# -----------------------------------------------------------------------------
source /opt/ros/diamondback/setup.bash
export ROS_LOCAL=/home/albert/ros
export ROS_PACKAGE_PATH=$ROS_LOCAL:$ROS_PACKAGE_PATH
export ROS_MASTER_URI=http://felis:11311

# -----------------------------------------------------------------------------
# MCT setings
# -----------------------------------------------------------------------------
export MCT_RESOURCES=/home/albert/.mct
export MCT_NAME=$ROS_LOCAL/mct
export MCT_CONFIG=$ROS_LOCAL/mct_config
export MCT_INSTALL_SCRIPTS=$MCT_NAME/mct_install/scripts
export MCT_PYTHON_VIRTUALENV=$MCT_RESOURCES/pyenv/mct
export MCT_EXTERNAL_PACKAGE_DIR=$MCT_RESOURCES/external_packages
