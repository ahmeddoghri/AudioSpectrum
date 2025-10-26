"""
Audio Spectrum Visualization Modes 201-225
Auto-generated from audio_spectrum_creative.py
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes201_225(BaseModeVisualizer):
    """Visualization modes 201 through 225"""

    def __init__(self, visualizer):
        super().__init__(visualizer)
        # Mode-specific state initialization will be added here
        # This ensures backward compatibility with the original code

    def draw_mode_201_meteor_net(self, frame, magnitudes):
        """Mode 201: Meteor Net - hex net catches meteors; nodes glow by band"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        size = 24
        for y in range(100, self.height-100, size):
            for x in range(80, self.width-80, size):
                idx = ((x+y)//size) % len(magnitudes)
                glow = int(80 + magnitudes[idx]*175)
                cv2.circle(frame,(x,y),3,(glow,glow,255),-1)
        if np.max(magnitudes)>0.9:
            cv2.circle(frame,(self.center_x,self.center_y),int(80 + bass*140),(255,255,255),1)
        return frame


    def draw_mode_202_deep_space_garden_hose(self, frame, magnitudes):
        """Mode 202: Deep-Space Garden Hose - spray pressure by amplitude; droplets chime on highs"""
        amp = float(np.mean(magnitudes))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        for i in range(int(30 + amp*120)):
            ang = -np.pi/6 + np.random.random()*np.pi/3
            r = 10 + np.random.random()* (120 + amp*200)
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),1,(200,200,255),-1)
        if highs>0.6:
            for _ in range(8):
                cv2.circle(frame,(np.random.randint(self.center_x-80,self.center_x+80), np.random.randint(self.center_y-80,self.center_y+80)),1,(255,255,200),-1)
        return frame


    def draw_mode_203_horizon_monoliths(self, frame, magnitudes):
        """Mode 203: Horizon Monoliths - distant monoliths rise with band; shadow sweeps on kicks"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        base_y = self.height-80
        count = min(20, len(magnitudes))
        gap = self.width//(count+1)
        for i in range(count):
            h = int(magnitudes[i]*220)
            x = gap*(i+1)
            cv2.rectangle(frame,(x, base_y-h),(x+10, base_y),(80,80,120),-1)
        if bass>0.7:
            cv2.rectangle(frame,(0,base_y-10),(self.width,base_y),(30,30,30),-1)
        return frame


    def draw_mode_204_gravity_slingshot_trails(self, frame, magnitudes):
        """Mode 204: Gravity Slingshot Trails - probes slingshot around planet; trail length by highs"""
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        for i in range(10):
            ang = self.frame_counter*0.02 + i*0.6
            r = 120 + i*6
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            for t in range(int(10 + highs*30)):
                px = int(self.center_x + np.cos(ang - t*0.02)*r)
                py = int(self.center_y + np.sin(ang - t*0.02)*r)
                cv2.circle(frame,(px,py),1,(140,140,255),-1)
            cv2.circle(frame,(x,y),2,(255,255,255),-1)
        return frame


    def draw_mode_205_solar_flare_notches(self, frame, magnitudes):
        """Mode 205: Solar Flare Notches - solar disc with notch flares per bin"""
        cv2.circle(frame,(self.center_x,self.center_y),120,(200,180,140),-1)
        bins = len(magnitudes)
        for i in range(0,bins, max(1,bins//60)):
            ang = (i/bins)*2*np.pi
            flare = int(magnitudes[i]*100)
            x1 = int(self.center_x + np.cos(ang)*120)
            y1 = int(self.center_y + np.sin(ang)*120)
            x2 = int(self.center_x + np.cos(ang)*(120+flare))
            y2 = int(self.center_y + np.sin(ang)*(120+flare))
            cv2.line(frame,(x1,y1),(x2,y2),(255,220,180),2, lineType=cv2.LINE_AA)
        return frame


    def draw_mode_206_tesseract_window(self, frame, magnitudes):
        """Mode 206: Tesseract Window - 4D cube projection; face alpha by band energy"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        size = int(80 + bass*80)
        for dz in (-1,1):
            for dy in (-1,1):
                for dx in (-1,1):
                    x = self.center_x + dx*size
                    y = self.center_y + dy*size
                    cv2.circle(frame,(x+dz*20,y+dz*10),2,(200,200,255),-1)
        for a in range(0,360,30):
            x1 = int(self.center_x + np.cos(np.radians(a))*size)
            y1 = int(self.center_y + np.sin(np.radians(a))*size)
            x2 = int(self.center_x + np.cos(np.radians(a+30))*size)
            y2 = int(self.center_y + np.sin(np.radians(a+30))*size)
            cv2.line(frame,(x1,y1),(x2,y2),(180,180,255),1)
        return frame


    def draw_mode_207_interstellar_postcards(self, frame, magnitudes):
        """Mode 207: Interstellar Postcards - tiles flip; each hosts tiny spectrum motif"""
        rows, cols = 3, 4
        tile_w = self.width//(cols+1)
        tile_h = self.height//(rows+1)
        for r in range(rows):
            for c in range(cols):
                x = (c+1)*tile_w - tile_w//2
                y = (r+1)*tile_h - tile_h//2
                cv2.rectangle(frame,(x-60,y-40),(x+60,y+40),(220,220,220),2)
                for k in range(8):
                    idx = (k*len(magnitudes)//8)
                    h = int(magnitudes[idx]*30)
                    cv2.line(frame,(x-50+k*12,y+20),(x-50+k*12,y+20-h),(150,200,255),2)
        return frame


    def draw_mode_208_cosmic_braille(self, frame, magnitudes):
        """Mode 208: Cosmic Braille - raised dots scroll; dot height by band"""
        for i in range(min(40,len(magnitudes))):
            x = int((i/40)*self.width)
            y = int(self.center_y + np.sin(self.frame_counter*0.05 + i)*40)
            size = max(1,int(1 + magnitudes[i]*6))
            cv2.circle(frame,(x,y),size,(200,200,255),-1)
        return frame


    def draw_mode_209_stellar_harpoon(self, frame, magnitudes):
        """Mode 209: Stellar Harpoon - line tension by amplitude; vibrato with highs"""
        amp = float(np.mean(magnitudes))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        length = int(80 + amp*260)
        wiggle = int(highs*20)
        x2 = int(self.center_x + length)
        y2 = int(self.center_y + np.sin(self.frame_counter*0.2)*wiggle)
        cv2.line(frame,(self.center_x,self.center_y),(x2,y2),(220,220,255),2)
        return frame


    def draw_mode_210_galaxy_ticker_tape(self, frame, magnitudes):
        """Mode 210: Galaxy Ticker Tape - ticker snakes; character scale by band"""
        for i in range(min(30,len(magnitudes))):
            x = int((self.frame_counter*2 + i*20) % (self.width+60)) - 60
            y = int(self.center_y + np.sin(i*0.3 + self.frame_counter*0.05)*40)
            s = int(6 + magnitudes[i]*16)
            cv2.rectangle(frame,(x,y),(x+s,y+s),(200,200,255),-1)
        return frame


    def draw_mode_211_antimatter_chess(self, frame, magnitudes):
        """Mode 211: Antimatter Chess - pieces phase in/out; height maps to band"""
        size = 40
        for r in range(8):
            for c in range(8):
                x = c*size+160
                y = r*size+160
                color = (40,40,60) if (r+c)%2==0 else (20,20,30)
                cv2.rectangle(frame,(x,y),(x+size,y+size),color,-1)
        for i in range(16):
            idx = i*(len(magnitudes)//16)
            h = int(magnitudes[idx]*30)
            x = 160 + (i%8)*size + 10
            y = 160 + (i//8)*size + 10
            cv2.rectangle(frame,(x,y-h),(x+20,y),(200,200,255),-1)
        return frame


    def draw_mode_212_star_nursery_conveyor(self, frame, magnitudes):
        """Mode 212: Star Nursery Conveyor - progression speed from energy"""
        energy = float(np.mean(magnitudes))
        for i in range(6):
            x = int((self.frame_counter*(2+energy*8) + i*140) % (self.width+160)) - 80
            for s in range(3):
                r = 8 + s*6
                cv2.circle(frame,(x, 220+s*40), r, (180,180,255), 2)
        return frame


    def draw_mode_213_magnetar_lines(self, frame, magnitudes):
        """Mode 213: Magnetar Lines - field lines whip; gamma flashes on transients"""
        for i in range(30):
            ang = i/30*2*np.pi
            k = np.sin(self.frame_counter*0.05 + i)*40
            x1 = int(self.center_x + np.cos(ang)*80)
            y1 = int(self.center_y + np.sin(ang)*80)
            x2 = int(self.center_x + np.cos(ang)*(180+k))
            y2 = int(self.center_y + np.sin(ang)*(180+k))
            cv2.line(frame,(x1,y1),(x2,y2),(160,200,255),1)
        if np.max(np.abs(np.diff(magnitudes)))>0.4:
            cv2.rectangle(frame,(0,0),(self.width,self.height),(255,255,255),1)
        return frame


    def draw_mode_214_zero_kelvin_diamonds(self, frame, magnitudes):
        """Mode 214: Zero-Kelvin Diamonds - refracted beams thickness tracks bands; spin with tempo"""
        angle = self.frame_counter*0.02
        for i in range(6):
            t = i/6
            r = int(40 + t*160)
            x = int(self.center_x + np.cos(angle+t*2*np.pi)*r)
            y = int(self.center_y + np.sin(angle+t*2*np.pi)*r)
            cv2.polylines(frame,[np.array([(x,y-10),(x+10,y),(x,y+10),(x-10,y)],np.int32)],True,(200,220,255),2)
        return frame


    def draw_mode_215_orbital_time_garden(self, frame, magnitudes):
        """Mode 215: Orbital Time Garden - planets are clock markers; orbits expand with bass"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        for h in range(12):
            ang = h/12*2*np.pi - np.pi/2
            r = int(120 + bass*60)
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),6,(200,200,255),-1)
        return frame


    def draw_mode_216_subspace_ribbon_printer(self, frame, magnitudes):
        """Mode 216: Subspace Ribbon Printer - ribbon thickness equals summed band energy at slice"""
        total = float(np.sum(magnitudes))
        y = int(120 + (self.frame_counter % (self.height-240)))
        thickness = int(4 + total*8)
        cv2.line(frame,(60,y),(self.width-60,y),(200,200,255),thickness)
        return frame


    def draw_mode_217_dark_matter_drizzle(self, frame, magnitudes):
        """Mode 217: Dark-Matter Drizzle - invisible drizzle reveals when bands exceed threshold"""
        thr = 0.5
        for i in range(len(magnitudes)):
            if magnitudes[i] > thr and np.random.random()<0.2:
                x = np.random.randint(0,self.width)
                y = np.random.randint(0,self.height)
                cv2.circle(frame,(x,y),1,(200,200,255),-1)
        if np.max(magnitudes)>0.9:
            cv2.circle(frame,(self.center_x,self.center_y),100,(100,100,100),1)
        return frame


    def draw_mode_218_meteor_choir_cones(self, frame, magnitudes):
        """Mode 218: Meteor Choir Cones - cone aperture by band; inner rings harmonics"""
        count = 8
        for i in range(count):
            idx = i*(len(magnitudes)//count)
            mag = magnitudes[idx]
            ang = (i/count)*2*np.pi
            x = int(self.center_x + np.cos(ang)*80)
            y = int(self.center_y + np.sin(ang)*80)
            rad = int(20 + mag*40)
            cv2.circle(frame,(x,y),rad,(200,200,255),1)
            cv2.circle(frame,(x,y),rad//2,(160,160,255),1)
        return frame


    def draw_mode_219_folded_galaxy_map(self, frame, magnitudes):
        """Mode 219: Folded Galaxy Map - folds reveal bar clusters; refolds during breakdown"""
        phase = (np.sin(self.frame_counter*0.03)+1)/2
        cols = 12
        for i in range(cols):
            x = int(80 + i*(self.width-160)/cols)
            h = int(magnitudes[min(i,len(magnitudes)-1)]*200*phase)
            cv2.rectangle(frame,(x,self.center_y-h),(x+6,self.center_y+h),(200,200,255),-1)
        return frame


    def draw_mode_220_ion_thruster_plume(self, frame, magnitudes):
        """Mode 220: Ion Thruster Plume - plume length maps to amplitude; shock diamonds on peaks"""
        amp = float(np.mean(magnitudes))
        length = int(60 + amp*260)
        base = (120, self.center_y)
        cv2.rectangle(frame,(base[0]-10,base[1]-10),(base[0],base[1]+10),(180,180,200),-1)
        for i in range(10):
            y = base[1] - 20 + i*4
            cv2.line(frame,(base[0],y),(base[0]+length,y),(200,220,255),1)
        if np.max(magnitudes)>0.85:
            for i in range(5):
                x = base[0] + int(length*(i+1)/6)
                cv2.circle(frame,(x,base[1]),3,(255,255,255),-1)
        return frame


    def draw_mode_221_cosmic_dominoes(self, frame, magnitudes):
        """Mode 221: Cosmic Dominoes - curved domino line; fall rate by energy; tiles display local bars"""
        energy = float(np.mean(magnitudes))
        n = 20
        for i in range(n):
            t = i/n
            ang = t*np.pi
            x = int(120 + t*(self.width-240))
            y = int(self.center_y + np.sin(ang)*60)
            tilt = int(np.sin(self.frame_counter*0.02 + t*6)*energy*30)
            pts = np.array([(x-10,y-20),(x+10,y-20+tilt),(x+10,y+20+tilt),(x-10,y+20)],np.int32)
            cv2.polylines(frame,[pts],True,(200,200,255),2)
        return frame


    def draw_mode_222_spacesuit_hud(self, frame, magnitudes):
        """Mode 222: Spacesuit HUD - HUD overlays with spectrum wedges; warning flashes on peaks"""
        wedges = 24
        for i in range(wedges):
            t = i/wedges
            idx = min(int(t*len(magnitudes)), len(magnitudes)-1)
            h = int(magnitudes[idx]*80)
            ang1 = int(t*360)
            ang2 = ang1 + 6
            cv2.ellipse(frame,(self.center_x,self.center_y),(200,200),-90,ang1,ang2,(150,200,255),2)
            cv2.ellipse(frame,(self.center_x,self.center_y),(200+h,200+h),-90,ang1,ang2,(200,220,255),2)
        if np.max(magnitudes)>0.9:
            cv2.circle(frame,(self.center_x,self.center_y),10,(0,0,255),-1)
        return frame


    def draw_mode_223_pulsar_barcode_beam(self, frame, magnitudes):
        """Mode 223: Pulsar Barcode Beam - rotating beam; bar lengths by band; bloom on peaks"""
        angle = (self.frame_counter*2) % 360
        bars = 48
        for i in range(bars):
            t = i/bars
            idx = min(int(t*len(magnitudes)), len(magnitudes)-1)
            r = int(60 + magnitudes[idx]*200)
            ang = np.radians(angle) + t*2*np.pi
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),1,(200,200,255),-1)
        if np.max(magnitudes)>0.85:
            cv2.circle(frame,(self.center_x,self.center_y),40,(255,255,255),1)
        return frame


    def draw_mode_224_astro_terrarium(self, frame, magnitudes):
        """Mode 224: Astro Terrarium - micro planet ecosystem; eruptions on kicks; biolume with highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        cv2.circle(frame,(self.center_x,self.center_y+60),90,(80,120,80),-1)
        if bass>0.7:
            for _ in range(30):
                x = self.center_x + np.random.randint(-60,60)
                y = self.center_y + 60 - np.random.randint(0,60)
                cv2.circle(frame,(x,y),2,(160,80,60),-1)
        for _ in range(int(highs*40)):
            cv2.circle(frame,(np.random.randint(self.center_x-80,self.center_x+80), np.random.randint(self.center_y-20,self.center_y+120)),1,(120,220,200),-1)
        return frame


    def draw_mode_225_micrometeor_spark_curtain(self, frame, magnitudes):
        """Mode 225: Micrometeor Spark Curtain - diagonal sparks; density with amplitude"""
        amp = float(np.mean(magnitudes))
        density = int(40 + amp*200)
        for _ in range(density):
            x = np.random.randint(0,self.width)
            y = np.random.randint(0,self.height)
            dx = 6; dy = 12
            cv2.line(frame,(x,y),(x+dx,y+dy),(200,200,255),1)
        return frame


