# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "swin_detection: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iswin_detection:/home/liudiyang/sp/ros/src/swin_detection/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(swin_detection_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" NAME_WE)
add_custom_target(_swin_detection_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "swin_detection" "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" "sensor_msgs/Image:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(swin_detection
  "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/swin_detection
)

### Generating Services

### Generating Module File
_generate_module_cpp(swin_detection
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/swin_detection
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(swin_detection_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(swin_detection_generate_messages swin_detection_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" NAME_WE)
add_dependencies(swin_detection_generate_messages_cpp _swin_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(swin_detection_gencpp)
add_dependencies(swin_detection_gencpp swin_detection_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS swin_detection_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(swin_detection
  "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/swin_detection
)

### Generating Services

### Generating Module File
_generate_module_eus(swin_detection
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/swin_detection
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(swin_detection_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(swin_detection_generate_messages swin_detection_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" NAME_WE)
add_dependencies(swin_detection_generate_messages_eus _swin_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(swin_detection_geneus)
add_dependencies(swin_detection_geneus swin_detection_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS swin_detection_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(swin_detection
  "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/swin_detection
)

### Generating Services

### Generating Module File
_generate_module_lisp(swin_detection
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/swin_detection
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(swin_detection_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(swin_detection_generate_messages swin_detection_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" NAME_WE)
add_dependencies(swin_detection_generate_messages_lisp _swin_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(swin_detection_genlisp)
add_dependencies(swin_detection_genlisp swin_detection_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS swin_detection_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(swin_detection
  "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/swin_detection
)

### Generating Services

### Generating Module File
_generate_module_nodejs(swin_detection
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/swin_detection
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(swin_detection_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(swin_detection_generate_messages swin_detection_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" NAME_WE)
add_dependencies(swin_detection_generate_messages_nodejs _swin_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(swin_detection_gennodejs)
add_dependencies(swin_detection_gennodejs swin_detection_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS swin_detection_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(swin_detection
  "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/swin_detection
)

### Generating Services

### Generating Module File
_generate_module_py(swin_detection
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/swin_detection
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(swin_detection_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(swin_detection_generate_messages swin_detection_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/liudiyang/sp/ros/src/swin_detection/msg/Object.msg" NAME_WE)
add_dependencies(swin_detection_generate_messages_py _swin_detection_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(swin_detection_genpy)
add_dependencies(swin_detection_genpy swin_detection_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS swin_detection_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/swin_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/swin_detection
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(swin_detection_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(swin_detection_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(swin_detection_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/swin_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/swin_detection
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(swin_detection_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(swin_detection_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(swin_detection_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/swin_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/swin_detection
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(swin_detection_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(swin_detection_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(swin_detection_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/swin_detection)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/swin_detection
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(swin_detection_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(swin_detection_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(swin_detection_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/swin_detection)
  install(CODE "execute_process(COMMAND \"/home/liudiyang/Application/miniconda3/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/swin_detection\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/swin_detection
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(swin_detection_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(swin_detection_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(swin_detection_generate_messages_py std_msgs_generate_messages_py)
endif()
