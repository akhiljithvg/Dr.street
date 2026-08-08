from setuptools import find_packages, setup

package_name = 'ds_simulation'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akhiljith',
    maintainer_email='akhiljithvg444@gmail.com',
    description='Gazebo simulation for the Dr.Street lane-following robot',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'sim_motor_bridge = ds_simulation.sim_motor_bridge:main',
        ],
    },
)
