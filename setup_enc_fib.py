__author__ = 'ramon'

#To install this setup just open the terminal and write:
#   python setup.py install

from cx_Freeze import setup, Executable

executables = [
    Executable("enc_fibo.py",
               #icon="logo.ico",
               appendScriptToExe=True,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

setup(name="enc_fibo",
      version="0.1",
      description="Encriptando utilizando Fibonacci",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )