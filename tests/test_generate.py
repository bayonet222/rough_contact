import unittest
import numpy as np
import brown.params as bp
import brown.generate as bg
import brown.analyse as ba


class TestSurfaceGeneration(unittest.TestCase):

    def setUp(self):
        self.N, self.dxy, self.val_init = 100, 1.0, 1.0
        self.L = self.dxy*self.N                

    def test_self_affine(self):
        surface_params = bp.self_affine_default_parameters()
        power_of_two = 9
        surface = bg.self_affine(surface_params, power_of_two)
        N = 2**power_of_two
        assert surface.shape[0] == surface.shape[1] == N
        # TODO this should be able to take the surface directly, make it numpy array compatible
        surface_spectrum = ba.radially_averaged_psd(surface.h, N/10000.)
        surface_invariants = ba.self_affine_psd_fit(*surface_spectrum)
        surface_hurst = surface_invariants[1]
        assert abs(surface_params.hurst - surface_hurst) < 0.1

     

if __name__ == '__main__':
    unittest.main()
