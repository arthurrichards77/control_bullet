"""
Execute step input on elevator and record step response in log
"""
from fgclient import FgClient
c = FgClient()

# require level flight to begin
vs = c.vertical_speed_fps()
if abs(vs) > 0.2:
    raise ValueError('Vertical speed too large: ', vs)
# and require zero elevator
el = c.get_elevator()
if el != 0.0:
    raise ValueError('Elevator not central: ', el)

c.ap_pitch_off()

time_step = 0.5
for kk in range(120):
    c.tic()
    vs = c.vertical_speed_fps()
    if kk < 10:
        el = 0.0
    else:
        el = -0.02
    c.set_elevator(el)
    print(kk, el, vs)
    c.toc(0.5)

c.set_elevator(0.0)
c.ap_pitch_vs(0.0)
