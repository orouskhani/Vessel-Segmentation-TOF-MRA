import argparse

import itk
from distutils.version import StrictVersion as VS

parser = argparse.ArgumentParser(description="Segment blood vessels.")
parser.add_argument("input_image")
parser.add_argument("output_image")
parser.add_argument("--sigma", type=float, default=1.0)
parser.add_argument("--alpha1", type=float, default=0.5)
parser.add_argument("--alpha2", type=float, default=2.0)
args = parser.parse_args()

input_image = itk.imread(args.input_image, itk.ctype("float"))

hessian_image = itk.hessian_recursive_gaussian_image_filter(
    input_image, sigma=args.sigma
)

vesselness_filter = itk.Hessian3DToVesselnessMeasureImageFilter[
    itk.ctype("float")
].New()
vesselness_filter.SetInput(hessian_image)
vesselness_filter.SetAlpha1(args.alpha1)
vesselness_filter.SetAlpha2(args.alpha2)

itk.imwrite(vesselness_filter, args.output_image)