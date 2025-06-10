from ase.build import bulk
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword

#create Cobalt Bulk Structure
latt = 2.30
Cobulk = bulk( 'Co', 'hcp', a = latt, c = 1.62753*latt)

#Cobulk.positions=([[0. ,0. ,0. ], [1.23060, 0.7104873, 0. ]])

# Create `pwscf` object for `Cobulk`
pwscf = PWscfInput ( Cobulk )

#Change the calculation to scf
update_keyword( pwscf.control.settings, 'calculation', 'scf' )

update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

update_keyword( pwscf.control.settings, 'prefix', 'scf' )
update_keyword( pwscf.control.io, 'disk_io', 'default')
update_keyword( pwscf.control.io,'wf_collect',False)

mass = [ 58.933195 ]
pseudo_potential = [ 'Co.pbe-n-kjpaw_psl.1.0.0.UPF' ]
update_keyword( pwscf.atomic_species, 'mass', mass )
update_keyword( pwscf.atomic_species, 'pseudo_potential', pseudo_potential )

update_keyword( pwscf.system.occupations,'degauss', 0.007)
update_keyword( pwscf.system.occupations,'smearing','fd')


update_keyword( pwscf.kpoints, 'mesh', [16,16,16] )
update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.ecut, 'ecutwfc', 65.0)
update_keyword( pwscf.system.ecut, 'ecutrho', 4*65.0)
write_pwscf_input( pwscf, "scf_A_230.inp")
