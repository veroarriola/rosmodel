from setuptools import setup

package_name = 'rosmodel'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, 'state'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['db.sqlite3']),
    ],
    install_requires=['setuptools','django >= 4.0'],
    zip_safe=True,
    maintainer='blackzafiro',
    maintainer_email='v.arriola@ciencias.unam.mx',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dbstate = rosmodel.dbstate:main'
        ],
    },
)
