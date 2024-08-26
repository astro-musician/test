def hubble(redshift, cosmo_dict):
    H0 = cosmo_dict["H0"]
    Wm = cosmo_dict["omega_m_0"] * (1 + redshift) ** 3
    K = cosmo_dict["K_0"] * (1 + redshift) ** 2
    DE = cosmo_dict["omega_lambda_0"]

    return H0 * np.sqrt(Wm + K + DE)
