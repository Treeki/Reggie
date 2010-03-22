from distutils.core import setup
from distutils.extension import Extension

setup(
  name='nsmblib',
  version='0.4',
  ext_modules=[
    Extension(
      'nsmblib',
      ['nsmblibmodule.c'],
    )
  ]
)
