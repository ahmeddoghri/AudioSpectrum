"""
Audio Spectrum Visualization Modes 226-275
Auto-generated from audio_spectrum_creative.py
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes226_275(BaseModeVisualizer):
    """Visualization modes 226 through 275"""

    def __init__(self, visualizer):
        super().__init__(visualizer)
        # Mode-specific state initialization will be added here
        # This ensures backward compatibility with the original code

    def draw_mode_226_golden_phyllotaxis_bloom(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        self.phyllotaxis_breath = 0.98*self.phyllotaxis_breath + 0.02*(0.8 + bass*0.6)
        dot_count = 1200
        angle_deg = self.phyllotaxis_angle
        scale = 2.0 * self.phyllotaxis_breath
        jitter = highs * 2.0
        for i in range(dot_count):
            a = np.radians(i*angle_deg)
            r = scale*np.sqrt(i)
            x = int(self.center_x + (r*np.cos(a)) + np.random.uniform(-jitter, jitter))
            y = int(self.center_y + (r*np.sin(a)) + np.random.uniform(-jitter, jitter))
            if 0 <= x < self.width and 0 <= y < self.height:
                frame[y, x] = (150, 180, 255)
        return frame


    def draw_mode_227_breathing_mandala_weave(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        tempo = float(np.mean(magnitudes))
        self.mandala_weave_phase += 0.01 + tempo*0.02
        segments = 12
        radius = int(120 + bass*120)
        for i in range(segments):
            ang = (i/segments)*2*np.pi + self.mandala_weave_phase
            x1 = int(self.center_x + np.cos(ang)*radius)
            y1 = int(self.center_y + np.sin(ang)*radius)
            ang2 = ang + np.pi/segments
            x2 = int(self.center_x + np.cos(ang2)*radius)
            y2 = int(self.center_y + np.sin(ang2)*radius)
            cv2.line(frame,(x1,y1),(x2,y2),(200,180,255),2, lineType=cv2.LINE_AA)
        return frame


    def draw_mode_228_infinite_tunnel_lissajous(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        self.lissajous_t += 0.02
        for i in range(100):
            t = self.lissajous_t + i*0.1
            x = int(self.center_x + (120 + bass*100)*np.sin(t*1.0))
            y = int(self.center_y + (80 + mids*80)*np.sin(t*1.3))
            s = max(1, 6 - i//20)
            cv2.circle(frame,(x,y),s,(160,160,200),-1)
        return frame


    def draw_mode_229_lotus_bloom_cascade(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        rings = 8
        self.lotus_phase += 0.02
        for r in range(rings):
            phase = self.lotus_phase - r*0.1
            rad = int(40 + r*22 + bass*60*np.sin(phase))
            petals = 10
            for p in range(petals):
                ang = (p/petals)*2*np.pi
                x = int(self.center_x + np.cos(ang)*rad)
                y = int(self.center_y + np.sin(ang)*rad)
                color = (180, 200, 255)
                if highs>0.6 and p%3==0:
                    color = (220, 220, 255)
                cv2.circle(frame,(x,y),2,color,-1)
        return frame


    def draw_mode_230_orbital_hypno_pendula(self, frame, magnitudes):
        tempo = float(np.mean(magnitudes))
        count = 24
        if not self.hypno_pendula:
            for i in range(count):
                self.hypno_pendula.append({'phase':i*0.2})
        for i, p in enumerate(self.hypno_pendula):
            p['phase'] += 0.02 + tempo*0.02
            ang = p['phase']
            r = 160
            x = int(self.center_x + np.cos(ang+i*0.1)*r)
            y = int(self.center_y + np.sin(ang+i*0.1)*r)
            cv2.circle(frame,(x,y),3,(200,200,255),-1)
        return frame


    def draw_mode_231_moire_breathing_nets(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.moire_angle_a += 0.01
        self.moire_angle_b -= 0.012
        scale = 1.0 + bass*0.3
        step = 24
        for y in range(0, self.height, step):
            x1 = int(self.center_x + np.cos(self.moire_angle_a)*scale*(y-self.center_y))
            cv2.line(frame,(0,y),(self.width,y),(80,80,120),1)
            if 0 <= x1 < self.width:
                frame[y, x1] = (120, 120, 200)
        for x in range(0, self.width, step):
            y1 = int(self.center_y + np.sin(self.moire_angle_b)*scale*(x-self.center_x))
            cv2.line(frame,(x,0),(x,self.height),(80,80,120),1)
            if 0 <= y1 < self.height:
                frame[y1, x] = (120, 120, 200)
        return frame


    def draw_mode_232_spiral_shepard_rings(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.shepard_zoom *= 1.0 + (bass-0.5)*0.002
        for i in range(12):
            r = int((i+1)*20*self.shepard_zoom) % 240
            cv2.circle(frame,(self.center_x,self.center_y),r,(140,140,200),1)
        return frame


    def draw_mode_233_velvet_plasma_pool(self, frame, magnitudes):
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        self.plasma_shift += 0.01
        for y in range(0, self.height, 4):
            for x in range(0, self.width, 4):
                v = np.sin(x*0.01 + self.plasma_shift) + np.cos(y*0.01 - self.plasma_shift)
                c = int(120 + 40*v + highs*50)
                frame[y:y+4, x:x+4] = (c, c, 200)
        return frame


    def draw_mode_234_radial_pulse_cathedral(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.pulse_timer += 1
        if self.pulse_timer % int(max(5, 30 - bass*20)) == 0:
            for r in range(30, 260, 20):
                cv2.circle(frame,(self.center_x,self.center_y),r,(160,160,220),1)
        return frame


    def draw_mode_235_s_curve_serpents(self, frame, magnitudes):
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        amp = 60 + int(mids*120)
        points = []
        for t in range(0, 360, 4):
            x = int(self.center_x + t - 180)
            y = int(self.center_y + np.sin((t/30)+self.frame_counter*0.05)*amp)
            points.append((x,y))
        for i in range(1,len(points)):
            cv2.line(frame, points[i-1], points[i], (200,180,255), 2, lineType=cv2.LINE_AA)
        return frame


    def draw_mode_236_orb_choir_orbitals(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        if not self.orb_choir:
            for i in range(20):
                self.orb_choir.append({'ang':i*0.3})
        for i, o in enumerate(self.orb_choir):
            o['ang'] += 0.01
            a = o['ang']
            r = 120 + int(bass*80)
            x = int(self.center_x + np.cos(a+i*0.1)*r)
            y = int(self.center_y + np.sin(a+i*0.13)*r*0.8)
            cv2.circle(frame,(x,y),3,(180,200,255),-1)
        return frame


    def draw_mode_237_sufi_spin_carpet(self, frame, magnitudes):
        self.sufi_spin_angle += 0.01
        for i in range(12):
            ang = self.sufi_spin_angle + i*0.5
            x1 = int(self.center_x + np.cos(ang)*180)
            y1 = int(self.center_y + np.sin(ang)*180)
            cv2.line(frame,(self.center_x,self.center_y),(x1,y1),(160,160,220),1)
        return frame


    def draw_mode_238_helmholtz_rings(self, frame, magnitudes):
        tempo = float(np.mean(magnitudes))
        self.helmholtz_phase += 0.01 + tempo*0.01
        for i in range(12):
            r = int(40 + i*16 + np.sin(self.helmholtz_phase + i*0.2)*12)
            cv2.circle(frame,(self.center_x,self.center_y),r,(180,180,240),1)
        return frame


    def draw_mode_239_hypno_slinky_stairwell(self, frame, magnitudes):
        self.slinky_depth += 0.6
        for i in range(40):
            t = (self.slinky_depth + i*12) % (self.height+80)
            y = int(t - 40)
            x = int(self.center_x + (i-20)*6)
            cv2.rectangle(frame,(x-20,y-6),(x+20,y+6),(120,120,180),1)
        return frame


    def draw_mode_240_fractal_fern_drift(self, frame, magnitudes):
        if len(self.fern_points) < 4000:
            x, y = 0.0, 0.0
            for _ in range(1000):
                r = np.random.random()
                if r < 0.01:
                    x, y = 0.0, 0.16*y
                elif r < 0.86:
                    x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
                elif r < 0.93:
                    x, y = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
                else:
                    x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
                self.fern_points.append((x,y))
        for px, py in self.fern_points[::10]:
            sx = int(self.center_x + px*60)
            sy = int(self.height-80 - py*60)
            if 0 <= sx < self.width and 0 <= sy < self.height:
                frame[sy, sx] = (160, 200, 160)
        return frame


    def draw_mode_241_binaural_circles(self, frame, magnitudes):
        left = float(np.mean(magnitudes[:len(magnitudes)//8]))
        right = float(np.mean(magnitudes[len(magnitudes)//8:len(magnitudes)//4]))
        self.binaural_phase_l += 0.02 + left*0.02
        self.binaural_phase_r += 0.021 + right*0.02
        rl = int(80 + np.sin(self.binaural_phase_l)*30)
        rr = int(80 + np.sin(self.binaural_phase_r)*30)
        cv2.circle(frame,(self.center_x-80,self.center_y),rl,(180,180,240),2)
        cv2.circle(frame,(self.center_x+80,self.center_y),rr,(180,180,240),2)
        return frame


    def draw_mode_242_auric_chakric_wheel(self, frame, magnitudes):
        self.chakric_phase += 0.01
        for i, ry in enumerate(range(self.center_y-180, self.center_y+220, 60)):
            r = int(30 + np.sin(self.chakric_phase + i*0.3)*20)
            cv2.circle(frame,(self.center_x, ry), r, (160,160,220), 2)
        return frame


    def draw_mode_243_hypersphere_ribbon(self, frame, magnitudes):
        self.hypersphere_phase += 0.02
        for i in range(120):
            t = i/120 * 2*np.pi
            x = int(self.center_x + 160*np.cos(t)*np.cos(self.hypersphere_phase))
            y = int(self.center_y + 90*np.sin(t)*np.sin(self.hypersphere_phase))
            frame[y, x] = (180, 180, 255)
        return frame


    def draw_mode_244_phi_step_kaleidos(self, frame, magnitudes):
        self.phi_kaleidos_phase += 0.02
        seg = 8
        for i in range(seg):
            ang = self.phi_kaleidos_phase + i*(2*np.pi/seg)
            x = int(self.center_x + np.cos(ang)*180)
            y = int(self.center_y + np.sin(ang)*180)
            cv2.line(frame,(self.center_x,self.center_y),(x,y),(160,160,220),1)
        return frame


    def draw_mode_245_silk_ribbon_cycloid(self, frame, magnitudes):
        self.cycloid_phase += 0.02
        for t in np.linspace(0, 4*np.pi, 200):
            x = int(self.center_x + 120*(np.cos(t) + 0.5*np.cos(2*t+self.cycloid_phase)))
            y = int(self.center_y + 80*(np.sin(t) - 0.5*np.sin(2*t+self.cycloid_phase)))
            if 0 <= x < self.width and 0 <= y < self.height:
                frame[y, x] = (200, 180, 255)
        return frame


    def draw_mode_246_oceanic_breather(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.ocean_swell = 0.98*self.ocean_swell + 0.02*(bass*60)
        for x in range(0, self.width, 6):
            y = int(self.center_y + np.sin(x*0.02 + self.frame_counter*0.04)* (20 + self.ocean_swell))
            cv2.line(frame,(x,y),(x,y+2),(160,200,255),1)
        return frame


    def draw_mode_247_zen_sand_harmonograph(self, frame, magnitudes):
        self.harmonograph_t += 0.02
        for t in np.linspace(0, 4*np.pi, 200):
            x = int(self.center_x + 140*np.sin(2*t + self.harmonograph_t))
            y = int(self.center_y + 100*np.sin(3*t))
            frame[y, x] = (200, 200, 255)
        return frame


    def draw_mode_248_magnetic_ink_veins(self, frame, magnitudes):
        if len(self.ink_veins) < 400:
            for _ in range(20):
                self.ink_veins.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height)})
        for v in self.ink_veins:
            v['x'] = (v['x'] + np.random.randint(-1,2)) % self.width
            v['y'] = (v['y'] + np.random.randint(-1,2)) % self.height
            frame[int(v['y']), int(v['x'])] = (180, 200, 220)
        return frame


    def draw_mode_249_breath_linked_vortex(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.breath_vortex = 0.98*self.breath_vortex + 0.02*(120 + bass*160)
        for a in np.linspace(0, 2*np.pi, 180):
            r = int(self.breath_vortex * (a/(2*np.pi)))
            x = int(self.center_x + np.cos(a)*r)
            y = int(self.center_y + np.sin(a)*r)
            frame[y, x] = (180, 180, 240)
        return frame


    def draw_mode_250_slow_meteor_carousel(self, frame, magnitudes):
        if not self.meteor_carousel:
            for i in range(18):
                self.meteor_carousel.append({'a':i*(2*np.pi/18)})
        for m in self.meteor_carousel:
            m['a'] += 0.005
            x = int(self.center_x + 160*np.cos(m['a']))
            y = int(self.center_y + 160*np.sin(m['a']))
            cv2.circle(frame,(x,y),2,(200,200,255),-1)
        return frame


    def draw_mode_251_ripple_glass_cathedral(self, frame, magnitudes):
        self.ripple_glass_phase += 0.02
        for y in range(0, self.height, 8):
            for x in range(0, self.width, 8):
                dx = int(2*np.sin(self.ripple_glass_phase + y*0.05))
                dy = int(2*np.cos(self.ripple_glass_phase + x*0.05))
                xx = min(self.width-1, max(0, x+dx))
                yy = min(self.height-1, max(0, y+dy))
                frame[y:y+8, x:x+8] = frame[yy:yy+8, xx:xx+8]
        return frame


    def draw_mode_252_theta_lantern_field(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        if len(self.theta_lanterns) < 40 and np.random.random()<0.3:
            self.theta_lanterns.append({'x':np.random.randint(40,self.width-40),'y':self.height+20,'vy':-1.0 - bass*1.5,'p':np.random.random()*2*np.pi})
        for lan in self.theta_lanterns[:]:
            lan['y'] += lan['vy']
            if lan['y'] < -40:
                self.theta_lanterns.remove(lan)
                continue
            r = int(10 + (np.sin(self.frame_counter*0.1 + lan['p'])+1)*4)
            cv2.circle(frame,(int(lan['x']),int(lan['y'])),r,(200,180,140),-1)
        return frame


    def draw_mode_253_isochromatic_weaves(self, frame, magnitudes):
        self.iso_weave_phase += 0.01
        for i in range(0,self.width,20):
            y = int(self.center_y + np.sin(i*0.03 + self.iso_weave_phase)*40)
            cv2.line(frame,(i,y-10),(i,y+10),(200,180,255),1)
        for j in range(0,self.height,20):
            x = int(self.center_x + np.cos(j*0.03 + self.iso_weave_phase)*40)
            cv2.line(frame,(x-10,j),(x+10,j),(180,200,255),1)
        return frame


    def draw_mode_254_orbiting_eye(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.orbiting_eye_angle += 0.01
        r = int(60 + bass*60)
        cv2.circle(frame,(self.center_x,self.center_y), r, (160,160,220), 2)
        x = int(self.center_x + np.cos(self.orbiting_eye_angle)*r)
        y = int(self.center_y + np.sin(self.orbiting_eye_angle)*r)
        cv2.circle(frame,(x,y),4,(220,220,255),-1)
        return frame


    def draw_mode_255_endless_ribbon_stair(self, frame, magnitudes):
        self.ribbon_stair_phase += 0.01
        for i in range(40):
            t = i/40
            x = int(self.center_x + (t-0.5)*300)
            y = int(self.center_y + np.sin(self.ribbon_stair_phase + t*6)*60)
            cv2.rectangle(frame,(x-6,y-20),(x+6,y+20),(160,160,220),1)
        return frame


    def draw_mode_256_glassy_toroidal_river(self, frame, magnitudes):
        self.toroidal_flow += 0.01
        for i in range(160):
            t = i/160
            ang = t*2*np.pi
            x = int(self.center_x + 160*np.cos(ang))
            y = int(self.center_y + 80*np.sin(ang) + np.sin(self.toroidal_flow+t*8)*6)
            frame[y, x] = (180, 200, 230)
        return frame


    def draw_mode_257_low_poly_hypno_shell(self, frame, magnitudes):
        self.hypno_shell_twist += 0.01
        for i in range(60):
            t = i/60
            r = int(40 + t*200)
            ang = self.hypno_shell_twist + t*6*np.pi
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),2,(200,200,240),-1)
        return frame


    def draw_mode_258_tide_clock_halo(self, frame, magnitudes):
        self.tide_clock_phase += 0.01
        r = int(120 + np.sin(self.tide_clock_phase)*20)
        cv2.circle(frame,(self.center_x,self.center_y),r,(160,160,220),2)
        ang = self.tide_clock_phase
        x = int(self.center_x + np.cos(ang)*r)
        y = int(self.center_y + np.sin(ang)*r)
        cv2.circle(frame,(x,y),4,(220,220,255),-1)
        return frame


    def draw_mode_259_morphic_kaleidofish(self, frame, magnitudes):
        if len(self.kaleidofish_school) < 50:
            for _ in range(50 - len(self.kaleidofish_school)):
                self.kaleidofish_school.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height),'vx':np.random.uniform(-1,1),'vy':np.random.uniform(-1,1)})
        for f in self.kaleidofish_school:
            f['x'] = (f['x'] + f['vx']) % self.width
            f['y'] = (f['y'] + f['vy']) % self.height
            frame[int(f['y']), int(f['x'])] = (200, 200, 255)
        return frame


    def draw_mode_260_zen_compass_waves(self, frame, magnitudes):
        self.compass_wave_phase += 0.01
        for i in range(8):
            ang = i*(np.pi/4)
            for r in range(40, 220, 20):
                x = int(self.center_x + np.cos(ang + self.compass_wave_phase)*r)
                y = int(self.center_y + np.sin(ang + self.compass_wave_phase)*r)
                cv2.circle(frame,(x,y),2,(180,180,230),-1)
        return frame


    def draw_mode_261_glacial_bloom(self, frame, magnitudes):
        if len(self.glacial_bloom) < 200:
            for _ in range(10):
                self.glacial_bloom.append({'x':self.center_x,'y':self.center_y,'vx':np.random.uniform(-1,1),'vy':np.random.uniform(-1,1),'life':200})
        for g in self.glacial_bloom[:]:
            g['x'] += g['vx']; g['y'] += g['vy']; g['life'] -= 1
            cv2.circle(frame,(int(g['x']),int(g['y'])),1,(200,220,255),-1)
            if g['life']<=0: self.glacial_bloom.remove(g)
        return frame


    def draw_mode_262_double_helix_lanterns(self, frame, magnitudes):
        if len(self.helix_lanterns) < 80:
            for i in range(80):
                self.helix_lanterns.append({'t':i*0.1})
        for h in self.helix_lanterns:
            h['t'] += 0.01
            x = int(self.center_x + 120*np.cos(h['t']))
            y = int(100 + (h['t']%(2*np.pi))/(2*np.pi) * (self.height-200))
            cv2.circle(frame,(x,y),2,(220,200,160),-1)
            x2 = int(self.center_x - 120*np.cos(h['t']))
            cv2.circle(frame,(x2,y),2,(220,200,160),-1)
        return frame


    def draw_mode_263_soft_grid_phase_slide(self, frame, magnitudes):
        self.soft_grid_phase += 0.01
        step = 30
        for y in range(0,self.height,step):
            for x in range(0,self.width,step):
                xx = x + int(4*np.sin(self.soft_grid_phase + y*0.05))
                yy = y + int(4*np.cos(self.soft_grid_phase + x*0.05))
                cv2.circle(frame,(xx,yy),1,(160,160,220),-1)
        return frame


    def draw_mode_264_ripple_dome_observatory(self, frame, magnitudes):
        self.ripple_dome_phase += 0.02
        for r in range(40, 260, 12):
            jitter = int(4*np.sin(self.ripple_dome_phase + r*0.05))
            cv2.circle(frame,(self.center_x,self.center_y), r+jitter, (160,160,230), 1)
        return frame


    def draw_mode_265_ethereal_spirocloud(self, frame, magnitudes):
        if len(self.spirocloud_traces) < 200:
            t = self.frame_counter*0.02
            x = int(self.center_x + 120*np.cos(2*t) + 40*np.cos(6*t))
            y = int(self.center_y + 80*np.sin(3*t) + 30*np.sin(5*t))
            self.spirocloud_traces.append((x,y))
        else:
            self.spirocloud_traces.pop(0)
        for i in range(1,len(self.spirocloud_traces)):
            a = int(i/len(self.spirocloud_traces)*200 + 55)
            cv2.line(frame,self.spirocloud_traces[i-1],self.spirocloud_traces[i],(a,a,255),1)
        return frame


    def draw_mode_266_mosaic_drizzle(self, frame, magnitudes):
        if not self.mosaic_cells:
            rows, cols = 18, 18
            for r in range(rows):
                for c in range(cols):
                    self.mosaic_cells.append({'r':r,'c':c,'val':np.random.randint(120,200)})
        for cell in self.mosaic_cells:
            if np.random.random()<0.01:
                cell['val'] = min(255, max(80, cell['val'] + np.random.randint(-5,6)))
            x = int(cell['c']*self.width/18)
            y = int(cell['r']*self.height/18)
            w = self.width//18
            h = self.height//18
            frame[y:y+h, x:x+w] = (cell['val'], cell['val'], 220)
        return frame


    def draw_mode_267_whispering_bamboo(self, frame, magnitudes):
        if not self.bamboo_stalks:
            for x in range(60, self.width, 60):
                self.bamboo_stalks.append({'x':x,'o':np.random.random()*6.28})
        for b in self.bamboo_stalks:
            sway = int(10*np.sin(self.frame_counter*0.03 + b['o']))
            cv2.line(frame,(b['x']+sway, self.height-40),(b['x']+sway, 160),(120,180,120),3)
        return frame


    def draw_mode_268_nesting_circles_flow(self, frame, magnitudes):
        self.nesting_circles_phase += 0.02
        for i in range(10):
            r = int(30 + i*18 + np.sin(self.nesting_circles_phase + i)*8)
            cv2.circle(frame,(self.center_x,self.center_y),r,(160,160,220),1)
        return frame


    def draw_mode_269_drifting_paper_cranes(self, frame, magnitudes):
        if not self.paper_cranes:
            for _ in range(24):
                self.paper_cranes.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height),'vx':np.random.uniform(-0.6,0.6),'vy':np.random.uniform(-0.3,0.0)})
        for c in self.paper_cranes:
            c['x'] = (c['x'] + c['vx']) % self.width
            c['y'] = (c['y'] + c['vy']) % self.height
            cv2.circle(frame,(int(c['x']),int(c['y'])),2,(220,220,240),-1)
        return frame


    def draw_mode_270_pulse_weave_hologrid(self, frame, magnitudes):
        self.pulse_hologrid_phase += 0.02
        for i in range(0,self.width,24):
            y = int(self.center_y + np.sin(self.pulse_hologrid_phase + i*0.05)*40)
            cv2.line(frame,(i,y-6),(i,y+6),(160,160,230),1)
        for j in range(0,self.height,24):
            x = int(self.center_x + np.cos(self.pulse_hologrid_phase + j*0.05)*40)
            cv2.line(frame,(x-6,j),(x+6,j),(160,160,230),1)
        return frame


    def draw_mode_271_serene_ribbon_canopy(self, frame, magnitudes):
        if not self.ribbon_canopy:
            for i in range(140):
                self.ribbon_canopy.append({'x':np.random.randint(0,self.width),'y':np.random.randint(-self.height,0)})
        for r in self.ribbon_canopy:
            r['y'] += 1
            if r['y'] > self.height:
                r['y'] = -np.random.randint(0,self.height)
            cv2.line(frame,(r['x'],r['y']),(r['x'],r['y']+8),(180,180,230),1)
        return frame


    def draw_mode_272_auroral_veil_gate(self, frame, magnitudes):
        self.auroral_gate_phase += 0.02
        for i in range(8):
            ang = i*(2*np.pi/8)
            for r in range(60, 220, 20):
                x = int(self.center_x + np.cos(ang + self.auroral_gate_phase)*r)
                y = int(self.center_y + np.sin(ang + self.auroral_gate_phase)*r)
                frame[y, x] = (180, 200, 255)
        return frame


    def draw_mode_273_satin_spiral_ladder(self, frame, magnitudes):
        self.satin_ladder_phase += 0.01
        for i in range(80):
            t = i/80
            ang = self.satin_ladder_phase + t*4*np.pi
            x = int(self.center_x + np.cos(ang)*140)
            y = int(self.center_y + np.sin(ang)*100)
            cv2.line(frame,(x-6,y),(x+6,y),(200,200,250),1)
        return frame


    def draw_mode_274_opaline_orb_drifter(self, frame, magnitudes):
        self.opaline_orb_t += 0.01
        x = int(self.center_x + np.sin(self.opaline_orb_t)*40)
        y = int(self.center_y - 30 + np.cos(self.opaline_orb_t*0.7)*20)
        cv2.circle(frame,(x,y), 60, (180, 200, 240), 2)
        return frame


    def draw_mode_275_hypno_quilt_loom(self, frame, magnitudes):
        self.quilt_loom_phase += 0.02
        step = 20
        for y in range(200, self.height-200, step):
            for x in range(100, self.width-100, step):
                if (x//step + y//step) % 2 == 0:
                    xx = int(x + 4*np.sin(self.quilt_loom_phase + y*0.05))
                    yy = int(y + 4*np.cos(self.quilt_loom_phase + x*0.05))
                    cv2.circle(frame,(xx,yy),1,(200,200,255),-1)
        return frame


