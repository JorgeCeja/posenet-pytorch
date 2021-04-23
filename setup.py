from setuptools import setup, find_packages
 
setup(
  name='posenet-pytorch',
  packages=find_packages(),
  version='0.1.0',
  license='Apache', 
  description='A PyTorch port of Google TensorFlow.js PoseNet (Real-time Human Pose Estimation)', 
  author='Ross Wightman',
  author_email='<Author Email>',
  url='https://github.com/rwightman/posenet-pytorch', 
  keywords=[
      'posenet', 
      'pose estimation'
  ], 
  install_requires=[
    'torch>=1.7.1',
    'opencv-python>=4.1.2',
    'requests>=2.25.1'
  ],
  classifiers=[
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Topic :: Scientific/Engineering :: Artificial Intelligence',
  'License :: OSI Approved :: Apache License',
  'Programming Language :: Python :: 3'
],
)