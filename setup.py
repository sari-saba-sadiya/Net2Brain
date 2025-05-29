from setuptools import setup, find_packages

setup(
    name = 'net2brain',
    version = '1.1.2',
    author = 'Roig Lab',
    packages=find_packages(),
    package_data={
        "": ["*.json"],
        "net2brain.architectures.configs": ["*.*"],
    },
    include_package_data=True,
    install_requires=[
        'h5py',
        'transformers',
        'einops',
        'accelerate',
        'matplotlib',
        'statsmodels',
        'requests',
        'seaborn==0.12.2',
        'pandas',
        'numpy',
        'Pillow',
        'prettytable',
        'gdown',
        'pycocotools',
        'pytest',
        'scikit_learn',
        'scipy',
        'torch',
        'tqdm',
        'visualpriors == 0.3.5',
        'timm == 0.4.12',
        'torchextractor == 0.3.0',
        'mit_semseg @ git+https://github.com/CSAILVision/semantic-segmentation-pytorch.git@master'
    ],
        extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "flake8",
        ],
    },
)
