import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cmocean

cm2 = '/home/lmella/Desktop/data_carpentry/data/pr_Amon_ACCESS-CM2_historical_r1i1p1f1_gn_201001-201412.nc'
esmi1 = '/home/lmella/Desktop/data_carpentry/data/pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_201001-201412.nc'
#Se crea una funcion para crear gráficos reutilizando codigo.

def plot_pr_climatology(pr_file, season, gridlines=False):
    """Plot the precipitation climatology. Args: pr_file (str): Precipitation data file season (str): Season (3 letter abbreviation, e.g. JJA) gridlines (bool): Select whether to plot gridlines """

    dset = xr.open_dataset(pr_file)

    clim = dset['pr'].groupby('time.season').mean('time', keep_attrs=True)

    clim.data = clim.data * 86400
    clim.attrs['units'] = 'mm/day'

    fig = plt.figure(figsize=[12,5])
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=180))
    clim.sel(season=season).plot.contourf(ax=ax,
                                          levels=np.arange(0, 13.5, 1.5),
                                          extend='max',
                                          transform=ccrs.PlateCarree(),
                                          cbar_kwargs={'label': clim.units},
                                          cmap=cmocean.cm.haline_r)
    ax.coastlines()
    if gridlines:
        plt.gca().gridlines()
    
    model = dset.attrs['source_id']
    title = f'{model} precipitation climatology ({season})'
    plt.title(title)

#%%pr_Amon_ACCESS-CM2_historical_r1i1p1f1_gn_201001-201412.nc
plot_pr_climatology(cm2, 'DJF')
plt.savefig('Precipitaciones Diciembre-Febrero')
#%%
plot_pr_climatology(cm2, 'MAM')
plt.savefig('Precipitaciones Marzo-Mayo')
#%%
plot_pr_climatology(cm2, 'JJA')
plt.savefig('Precipitaciones Junio-Agosto')
#%%
plot_pr_climatology(cm2, 'SON') 
plt.savefig('Precipitaciones Septiembre-Noviembre')

#%%pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_201001-201412.nc

plot_pr_climatology(esmi1, 'DJF')
plt.show()
#%%
plot_pr_climatology(esmi1, 'MAM')
plt.show()
#%%
plot_pr_climatology(esmi1, 'JJA')
plt.show()
#%%
plot_pr_climatology(esmi1, 'SON')
plt.show()





