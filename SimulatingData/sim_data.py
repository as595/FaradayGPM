import numpy as np  # for arrays


class FaradaySim:

	def __init__(self, nu, noise=0.0):

		self.nu = nu
		self.lam = 3e8/nu
		self.lam_sq = (3e8/nu)**2
		self.noise = noise

		return

	def FaradayThin(self, phi):

		"""
		Returns complex polarization as a function of
		wavelength-squared for a Faraday thin (delta function)
		Faraday structure

		Inputs:
		
		phi - Faraday depth of component

		"""

		P_rg = np.cos(2*phi*self.lam_sq) + 1j*np.sin(2*phi*self.lam_sq)
		P_rg+=np.random.normal(0,self.noise,len(P_rg))

		return P_rg


	def FaradayThick1(self, phi_fg):


		"""
		Returns complex polarization as a function of
		wavelength-squared for a Faraday thick (top hat function)
		Faraday structure centred on phi = 0

		Inputs:
		
		phi_fg - 0.5 x Faraday width of component

		"""

		P_gal = np.sin(2*phi_fg*self.lam_sq)/(2*phi_fg*self.lam_sq) + 0*1j
		P_gal+=np.random.normal(0,self.noise,len(P_gal))

		return P_gal