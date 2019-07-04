from setuptools import setup

setup(
    name='Cryocon-control',
    version='0.0.1',
    description='python package controls the Cryocon via the prologix GPIB to Ethernet adapter',
    license='MIT',
    packages=['cryocon', 'plx_gpib_ethernet'],
    author='Dr. Alexander Pollak',
    author_email='Alexander.Pollak.87@gmail.com',
    keywords=['Cryocon','GPIB'],
    url='https://github.com/AlexanderPollak/Cryocon-control'
)