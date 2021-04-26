%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-launch-ros
Version:        0.14.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS launch_ros package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       ros-galactic-ament-index-python
Requires:       ros-galactic-composition-interfaces
Requires:       ros-galactic-launch
Requires:       ros-galactic-lifecycle-msgs
Requires:       ros-galactic-osrf-pycommon
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-importlib-metadata
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-galactic-ament-copyright
BuildRequires:  ros-galactic-ament-flake8
BuildRequires:  ros-galactic-ament-index-python
BuildRequires:  ros-galactic-ament-pep257
BuildRequires:  ros-galactic-composition-interfaces
BuildRequires:  ros-galactic-launch
BuildRequires:  ros-galactic-lifecycle-msgs
BuildRequires:  ros-galactic-osrf-pycommon
BuildRequires:  ros-galactic-rclpy
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS specific extensions to the launch tool.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/galactic"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Mon Apr 26 2021 Jacob Perron <jacob@openrobotics.org> - 0.14.2-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Jacob Perron <jacob@openrobotics.org> - 0.14.1-2
- Autogenerated by Bloom

* Mon Apr 12 2021 Jacob Perron <jacob@openrobotics.org> - 0.14.1-1
- Autogenerated by Bloom

* Tue Apr 06 2021 Jacob Perron <jacob@openrobotics.org> - 0.14.0-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Jacob Perron <jacob@openrobotics.org> - 0.13.0-1
- Autogenerated by Bloom

