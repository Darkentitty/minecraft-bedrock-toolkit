import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json, os, shutil, uuid
from pathlib import Path

class MinecraftBedrockToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Bedrock Toolkit - Complete Edition")
        self.root.geometry("900x800")
        self.worlds_path = r"C:\Users\kilro\AppData\Roaming\Minecraft Bedrock\Users\3375517871852722159\games\com.mojang\minecraftWorlds"
        
        nb = ttk.Notebook(root)
        nb.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.create_minecart_tab(nb)
        self.create_effect_tab(nb)
        self.create_weather_tab(nb)
        self.create_loot_tab(nb)
        self.create_ore_tab(nb)
        self.create_structure_tab(nb)
    def create_minecart_tab(self, nb):
        f = ttk.Frame(nb, padding="10")
        nb.add(f, text="Minecart Speed")
        ttk.Label(f, text="Minecart Speed Modifier", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(f, text="Select World:").pack(anchor="w", padx=20, pady=(10,5))
        self.mc_w = tk.StringVar()
        mc_c = ttk.Combobox(f, textvariable=self.mc_w, width=70, state="readonly")
        mc_c.pack(padx=20)
        ttk.Button(f, text="Refresh", command=lambda: self.load_w(self.mc_w, mc_c)).pack(pady=5)
        ttk.Label(f, text="Speed:", font=("Arial", 12, "bold")).pack(pady=(15,5))
        self.mc_s = tk.DoubleVar(value=0.8)
        ttk.Scale(f, from_=0.4, to=10.0, variable=self.mc_s, orient=tk.HORIZONTAL, length=700).pack()
        mc_l = ttk.Label(f, text="", font=("Arial", 14, "bold"))
        mc_l.pack(pady=5)
        def u(*a): mc_l.config(text=f"{self.mc_s.get():.2f} ({self.mc_s.get()/0.4:.1f}x)")
        self.mc_s.trace("w", u)
        u()
        bf = ttk.Frame(f)
        bf.pack(pady=15)
        ttk.Button(bf, text="Install", command=self.inst_mc, width=20).pack(side="left", padx=5)
        ttk.Button(bf, text="Uninstall", command=self.uninst_mc, width=20).pack(side="left", padx=5)
        self.mc_log = scrolledtext.ScrolledText(f, width=100, height=15, state="disabled")
        self.mc_log.pack(pady=10)
        self.load_w(self.mc_w, mc_c)
    def create_effect_tab(self, nb):
        f = ttk.Frame(nb, padding="10")
        nb.add(f, text="Effect Cleaner")
        ttk.Label(f, text="Effect Cleaner", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(f, text="Select World:").pack(anchor="w", padx=20, pady=(10,5))
        self.ef_w = tk.StringVar()
        ef_c = ttk.Combobox(f, textvariable=self.ef_w, width=70, state="readonly")
        ef_c.pack(padx=20)
        ttk.Button(f, text="Refresh", command=lambda: self.load_w(self.ef_w, ef_c)).pack(pady=5)
        ttk.Label(f, text="Effects to Remove:", font=("Arial", 12, "bold")).pack(pady=(15,5))
        cf = ttk.Frame(f)
        cf.pack(pady=10)
        self.ef_mf = tk.BooleanVar(value=True)
        ttk.Checkbutton(cf, text="Mining Fatigue", variable=self.ef_mf).grid(row=0, column=0, sticky="w", padx=10)
        self.ef_sl = tk.BooleanVar(value=False)
        ttk.Checkbutton(cf, text="Slowness", variable=self.ef_sl).grid(row=1, column=0, sticky="w", padx=10)
        self.ef_wk = tk.BooleanVar(value=False)
        ttk.Checkbutton(cf, text="Weakness", variable=self.ef_wk).grid(row=2, column=0, sticky="w", padx=10)
        self.ef_ps = tk.BooleanVar(value=False)
        ttk.Checkbutton(cf, text="Poison", variable=self.ef_ps).grid(row=0, column=1, sticky="w", padx=10)
        self.ef_wt = tk.BooleanVar(value=False)
        ttk.Checkbutton(cf, text="Wither", variable=self.ef_wt).grid(row=1, column=1, sticky="w", padx=10)
        self.ef_ns = tk.BooleanVar(value=False)
        ttk.Checkbutton(cf, text="Nausea", variable=self.ef_ns).grid(row=2, column=1, sticky="w", padx=10)
        self.ef_bl = tk.BooleanVar(value=False)
        ttk.Checkbutton(cf, text="Blindness", variable=self.ef_bl).grid(row=0, column=2, sticky="w", padx=10)
        bf = ttk.Frame(f)
        bf.pack(pady=15)
        ttk.Button(bf, text="Install", command=self.inst_ef, width=20).pack(side="left", padx=5)
        ttk.Button(bf, text="Uninstall", command=self.uninst_ef, width=20).pack(side="left", padx=5)
        self.ef_log = scrolledtext.ScrolledText(f, width=100, height=15, state="disabled")
        self.ef_log.pack(pady=10)
        self.load_w(self.ef_w, ef_c)
    def create_weather_tab(self, nb):
        f = ttk.Frame(nb, padding="10")
        nb.add(f, text="Weather Control")
        ttk.Label(f, text="Weather Controller", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(f, text="Select World:").pack(anchor="w", padx=20, pady=(10,5))
        self.wt_w = tk.StringVar()
        wt_c = ttk.Combobox(f, textvariable=self.wt_w, width=70, state="readonly")
        wt_c.pack(padx=20)
        ttk.Button(f, text="Refresh", command=lambda: self.load_w(self.wt_w, wt_c)).pack(pady=5)
        ttk.Label(f, text="Lock Weather To:", font=("Arial", 12, "bold")).pack(pady=(15,5))
        self.wt_type = tk.StringVar(value="clear")
        rf = ttk.Frame(f)
        rf.pack(pady=10)
        ttk.Radiobutton(rf, text="Clear (No rain/thunder)", variable=self.wt_type, value="clear").pack(anchor="w", padx=20)
        ttk.Radiobutton(rf, text="Rain", variable=self.wt_type, value="rain").pack(anchor="w", padx=20)
        ttk.Radiobutton(rf, text="Thunder", variable=self.wt_type, value="thunder").pack(anchor="w", padx=20)
        ttk.Label(f, text="Weather will be locked permanently", font=("Arial", 9, "italic")).pack()
        bf = ttk.Frame(f)
        bf.pack(pady=15)
        ttk.Button(bf, text="Install", command=self.inst_wt, width=20).pack(side="left", padx=5)
        ttk.Button(bf, text="Uninstall", command=self.uninst_wt, width=20).pack(side="left", padx=5)
        self.wt_log = scrolledtext.ScrolledText(f, width=100, height=15, state="disabled")
        self.wt_log.pack(pady=10)
        self.load_w(self.wt_w, wt_c)
    def create_loot_tab(self, nb):
        f = ttk.Frame(nb, padding="10")
        nb.add(f, text="Loot Editor")
        ttk.Label(f, text="Loot Table Editor", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(f, text="Select World:").pack(anchor="w", padx=20, pady=(10,5))
        self.lt_w = tk.StringVar()
        lt_c = ttk.Combobox(f, textvariable=self.lt_w, width=70, state="readonly")
        lt_c.pack(padx=20)
        ttk.Button(f, text="Refresh", command=lambda: self.load_w(self.lt_w, lt_c)).pack(pady=5)
        ttk.Label(f, text="Loot Multiplier:", font=("Arial", 12, "bold")).pack(pady=(15,5))
        self.lt_m = tk.IntVar(value=2)
        ttk.Scale(f, from_=1, to=10, variable=self.lt_m, orient=tk.HORIZONTAL, length=700).pack()
        lt_l = ttk.Label(f, text="", font=("Arial", 14, "bold"))
        lt_l.pack(pady=5)
        def u(*a): lt_l.config(text=f"{self.lt_m.get()}x loot")
        self.lt_m.trace("w", u)
        u()
        bf = ttk.Frame(f)
        bf.pack(pady=15)
        ttk.Button(bf, text="Apply Full Chests", command=self.apply_lt, width=20).pack(side="left", padx=5)
        ttk.Button(bf, text="Restore Vanilla", command=self.restore_lt, width=20).pack(side="left", padx=5)
        self.lt_log = scrolledtext.ScrolledText(f, width=100, height=15, state="disabled")
        self.lt_log.pack(pady=10)
        self.load_w(self.lt_w, lt_c)
    def create_ore_tab(self, nb):
        f = ttk.Frame(nb, padding="10")
        nb.add(f, text="Ore Multiplier")
        ttk.Label(f, text="Ore Drop Multiplier", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(f, text="Select World:").pack(anchor="w", padx=20, pady=(10,5))
        self.or_w = tk.StringVar()
        or_c = ttk.Combobox(f, textvariable=self.or_w, width=70, state="readonly")
        or_c.pack(padx=20)
        ttk.Button(f, text="Refresh", command=lambda: self.load_w(self.or_w, or_c)).pack(pady=5)
        ttk.Label(f, text="Multiplier:", font=("Arial", 12, "bold")).pack(pady=(15,5))
        self.or_m = tk.IntVar(value=2)
        ttk.Scale(f, from_=1, to=20, variable=self.or_m, orient=tk.HORIZONTAL, length=700).pack()
        or_l = ttk.Label(f, text="", font=("Arial", 14, "bold"))
        or_l.pack(pady=5)
        def u(*a): or_l.config(text=f"{self.or_m.get()}x")
        self.or_m.trace("w", u)
        u()
        ttk.Label(f, text="Works on all vanilla ores", font=("Arial", 9, "italic")).pack()
        bf = ttk.Frame(f)
        bf.pack(pady=15)
        ttk.Button(bf, text="Install", command=self.inst_or, width=20).pack(side="left", padx=5)
        ttk.Button(bf, text="Uninstall", command=self.uninst_or, width=20).pack(side="left", padx=5)
        self.or_log = scrolledtext.ScrolledText(f, width=100, height=15, state="disabled")
        self.or_log.pack(pady=10)
        self.load_w(self.or_w, or_c)
    def create_structure_tab(self, nb):
        f = ttk.Frame(nb, padding="10")
        nb.add(f, text="Structure Spawn")
        ttk.Label(f, text="Structure Spawn Rate", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(f, text="Select World:").pack(anchor="w", padx=20, pady=(10,5))
        self.st_w = tk.StringVar()
        st_c = ttk.Combobox(f, textvariable=self.st_w, width=70, state="readonly")
        st_c.pack(padx=20)
        ttk.Button(f, text="Refresh", command=lambda: self.load_w(self.st_w, st_c)).pack(pady=5)
        ttk.Label(f, text="Spawn Rate:", font=("Arial", 12, "bold")).pack(pady=(15,5))
        self.st_m = tk.DoubleVar(value=1.0)
        ttk.Scale(f, from_=0.1, to=5.0, variable=self.st_m, orient=tk.HORIZONTAL, length=700).pack()
        st_l = ttk.Label(f, text="", font=("Arial", 14, "bold"))
        st_l.pack(pady=5)
        def u(*a): st_l.config(text=f"{self.st_m.get():.1f}x")
        self.st_m.trace("w", u)
        u()
        ttk.Label(f, text="Higher = more structures", font=("Arial", 9, "italic")).pack()
        bf = ttk.Frame(f)
        bf.pack(pady=15)
        ttk.Button(bf, text="Apply", command=self.apply_st, width=20).pack(side="left", padx=5)
        ttk.Button(bf, text="Restore", command=self.restore_st, width=20).pack(side="left", padx=5)
        self.st_log = scrolledtext.ScrolledText(f, width=100, height=15, state="disabled")
        self.st_log.pack(pady=10)
        self.load_w(self.st_w, st_c)
    def log(self, w, m):
        w.config(state="normal")
        w.insert(tk.END, m + "\n")
        w.see(tk.END)
        w.config(state="disabled")
    
    def load_w(self, v, c):
        try:
            ws = []
            for d in os.listdir(self.worlds_path):
                lf = os.path.join(self.worlds_path, d, "levelname.txt")
                if os.path.exists(lf):
                    with open(lf, encoding="utf-8") as f:
                        ws.append(f"{f.read().strip()} ({d})")
            c["values"] = ws
            if ws and not v.get(): c.current(0)
        except: pass
    
    def gwp(self, v):
        s = v.get()
        return os.path.join(self.worlds_path, s.split("(")[-1].rstrip(")")) if s else None
    def inst_mc(self):
        wp = self.gwp(self.mc_w)
        if not wp: return
        bf = Path(wp) / "behavior_packs" / "FastMinecarts"
        if bf.exists(): shutil.rmtree(bf)
        try:
            spd = self.mc_s.get()
            self.log(self.mc_log, f"Installing {spd/0.4:.1f}x...")
            bf.mkdir(parents=True, exist_ok=True)
            hid, mid = str(uuid.uuid4()), str(uuid.uuid4())
            with open(bf / "manifest.json", "w") as f:
                json.dump({"format_version": 2, "header": {"name": "Fast Minecarts", "description": f"{spd/0.4:.1f}x", "uuid": hid, "version": [1, 0, 0], "min_engine_version": [1, 20, 0]}, "modules": [{"type": "data", "uuid": mid, "version": [1, 0, 0]}]}, f, indent=2)
            ef = bf / "entities"
            ef.mkdir(exist_ok=True)
            ent = {"format_version": "1.12.0", "minecraft:entity": {"description": {"identifier": "minecraft:minecart", "is_spawnable": False, "is_summonable": True, "is_experimental": False}, "components": {"minecraft:is_stackable": {}, "minecraft:type_family": {"family": ["minecart", "inanimate"]}, "minecraft:collision_box": {"width": 0.98, "height": 0.7}, "minecraft:rail_movement": {"max_speed": spd}, "minecraft:rideable": {"seat_count": 1, "interact_text": "action.interact.ride.minecart", "pull_in_entities": True, "seats": {"position": [0.0, -0.2, 0.0]}}, "minecraft:rail_sensor": {"eject_on_activate": True}, "minecraft:physics": {}, "minecraft:pushable": {"is_pushable": True, "is_pushable_by_piston": True}, "minecraft:conditional_bandwidth_optimization": {"default_values": {"max_optimized_distance": 60.0, "max_dropped_ticks": 20, "use_motion_prediction_hints": False}, "conditional_values": [{"max_optimized_distance": 999.0, "max_dropped_ticks": 0, "conditional_values": [{"test": "is_moving", "subject": "self", "operator": "==", "value": True}]}]}}}}
            with open(ef / "minecart.json", "w") as f: json.dump(ent, f, indent=2)
            wbf = Path(wp) / "world_behavior_packs.json"
            wbd = json.load(open(wbf)) if wbf.exists() else []
            wbd = [p for p in wbd if p.get("pack_id") != hid]
            wbd.append({"pack_id": hid, "version": [1, 0, 0]})
            with open(wbf, "w") as f: json.dump(wbd, f, indent=2)
            self.log(self.mc_log, "Done! Restart, place NEW carts!")
            messagebox.showinfo("Success", "Installed!")
        except Exception as e:
            self.log(self.mc_log, f"ERROR: {e}")
    
    def uninst_mc(self):
        wp = self.gwp(self.mc_w)
        if not wp: return
        bf = Path(wp) / "behavior_packs" / "FastMinecarts"
        if bf.exists():
            shutil.rmtree(bf)
            self.log(self.mc_log, "Removed!")
            messagebox.showinfo("Success", "Removed!")
    def inst_ef(self):
        wp = self.gwp(self.ef_w)
        if not wp: return
        effects = []
        if self.ef_mf.get(): effects.append("mining_fatigue")
        if self.ef_sl.get(): effects.append("slowness")
        if self.ef_wk.get(): effects.append("weakness")
        if self.ef_ps.get(): effects.append("poison")
        if self.ef_wt.get(): effects.append("wither")
        if self.ef_ns.get(): effects.append("nausea")
        if self.ef_bl.get(): effects.append("blindness")
        if not effects:
            messagebox.showwarning("Warning", "Select at least one effect")
            return
        try:
            self.log(self.ef_log, f"Installing Effect Cleaner...")
            self.log(self.ef_log, f"Removing: {', '.join(effects)}")
            bf = Path(wp) / "behavior_packs" / "EffectCleaner"
            if bf.exists(): shutil.rmtree(bf)
            bf.mkdir(parents=True, exist_ok=True)
            hid, mid = str(uuid.uuid4()), str(uuid.uuid4())
            with open(bf / "manifest.json", "w") as f:
                json.dump({"format_version": 2, "header": {"name": "Effect Cleaner", "description": f"Removes: {', '.join(effects)}", "uuid": hid, "version": [1, 0, 0], "min_engine_version": [1, 20, 0]}, "modules": [{"type": "script", "language": "javascript", "uuid": mid, "version": [1, 0, 0], "entry": "scripts/main.js"}], "dependencies": [{"module_name": "@minecraft/server", "version": "1.8.0"}]}, f, indent=2)
            sf = bf / "scripts"
            sf.mkdir(exist_ok=True)
            elist = ', '.join([f'"{e}"' for e in effects])
            script = f"""import {{ system, world }} from '@minecraft/server';
const EFFECTS_TO_REMOVE = [{elist}];
system.runInterval(() => {{
    for (const player of world.getAllPlayers()) {{
        for (const effectId of EFFECTS_TO_REMOVE) {{
            try {{
                const effect = player.getEffect(effectId);
                if (effect) {{ player.removeEffect(effectId); }}
            }} catch (e) {{}}
        }}
    }}
}}, 1);
console.warn('[Effect Cleaner] Active! Removing: {', '.join(effects)}');"""
            with open(sf / "main.js", "w") as f: f.write(script)
            wbf = Path(wp) / "world_behavior_packs.json"
            wbd = json.load(open(wbf)) if wbf.exists() else []
            wbd = [p for p in wbd if p.get("pack_id") != hid]
            wbd.append({"pack_id": hid, "version": [1, 0, 0]})
            with open(wbf, "w") as f: json.dump(wbd, f, indent=2)
            self.log(self.ef_log, "Done! Restart world!")
            messagebox.showinfo("Success", f"Installed!\nRemoving: {', '.join(effects)}")
        except Exception as e:
            self.log(self.ef_log, f"ERROR: {e}")
    def uninst_ef(self):
        wp = self.gwp(self.ef_w)
        if not wp: return
        bf = Path(wp) / "behavior_packs" / "EffectCleaner"
        if bf.exists():
            shutil.rmtree(bf)
            self.log(self.ef_log, "Removed!")
            messagebox.showinfo("Success", "Removed!")
    def inst_wt(self):
        wp = self.gwp(self.wt_w)
        if not wp: return
        wtype = self.wt_type.get()
        try:
            self.log(self.wt_log, f"Installing Weather Controller...")
            self.log(self.wt_log, f"Locking weather to: {wtype}")
            bf = Path(wp) / "behavior_packs" / "WeatherController"
            if bf.exists(): shutil.rmtree(bf)
            bf.mkdir(parents=True, exist_ok=True)
            hid, mid = str(uuid.uuid4()), str(uuid.uuid4())
            with open(bf / "manifest.json", "w") as f:
                json.dump({"format_version": 2, "header": {"name": "Weather Controller", "description": f"Locks to: {wtype}", "uuid": hid, "version": [1, 0, 0], "min_engine_version": [1, 20, 0]}, "modules": [{"type": "script", "language": "javascript", "uuid": mid, "version": [1, 0, 0], "entry": "scripts/main.js"}], "dependencies": [{"module_name": "@minecraft/server", "version": "1.8.0"}]}, f, indent=2)
            sf = bf / "scripts"
            sf.mkdir(exist_ok=True)
            script = f"""import {{ system, world }} from '@minecraft/server';
system.runInterval(() => {{
    try {{
        const overworld = world.getDimension('overworld');
        overworld.runCommand('weather {wtype}');
    }} catch (e) {{
        console.warn('[Weather Controller] Error: ' + e);
    }}
}}, 100);
console.warn('[Weather Controller] Active! Weather locked to: {wtype}');"""
            with open(sf / "main.js", "w") as f: f.write(script)
            wbf = Path(wp) / "world_behavior_packs.json"
            wbd = json.load(open(wbf)) if wbf.exists() else []
            wbd = [p for p in wbd if p.get("pack_id") != hid]
            wbd.append({"pack_id": hid, "version": [1, 0, 0]})
            with open(wbf, "w") as f: json.dump(wbd, f, indent=2)
            self.log(self.wt_log, "Done! Restart world!")
            messagebox.showinfo("Success", f"Installed!\nWeather locked to: {wtype}")
        except Exception as e:
            self.log(self.wt_log, f"ERROR: {e}")
    def uninst_wt(self):
        wp = self.gwp(self.wt_w)
        if not wp: return
        bf = Path(wp) / "behavior_packs" / "WeatherController"
        if bf.exists():
            shutil.rmtree(bf)
            self.log(self.wt_log, "Removed!")
            messagebox.showinfo("Success", "Removed!")
    def apply_lt(self):
        wp = self.gwp(self.lt_w)
        if not wp: return
        mult = self.lt_m.get()
        try:
            self.log(self.lt_log, f"Applying {mult}x loot multiplier...")
            self.log(self.lt_log, "Scanning for loot tables...")
            bp_path = Path(wp) / "behavior_packs"
            modified = 0
            if bp_path.exists():
                for pack in bp_path.iterdir():
                    loot_path = pack / "loot_tables"
                    if loot_path.exists():
                        for loot_file in loot_path.rglob("*.json"):
                            try:
                                with open(loot_file, "r") as f:
                                    data = json.load(f)
                                if "pools" in data:
                                    for pool in data["pools"]:
                                        if "rolls" in pool:
                                            if isinstance(pool["rolls"], int):
                                                pool["rolls"] *= mult
                                            elif isinstance(pool["rolls"], dict) and "min" in pool["rolls"]:
                                                pool["rolls"]["min"] *= mult
                                                pool["rolls"]["max"] *= mult
                                    with open(loot_file, "w") as f:
                                        json.dump(data, f, indent=2)
                                    modified += 1
                                    self.log(self.lt_log, f"Modified: {loot_file.name}")
                            except: pass
            self.log(self.lt_log, f"Done! Modified {modified} loot tables")
            messagebox.showinfo("Success", f"Modified {modified} loot tables!")
        except Exception as e:
            self.log(self.lt_log, f"ERROR: {e}")
    def restore_lt(self):
        messagebox.showinfo("Info", "Restore vanilla loot by removing/reinstalling behavior packs")
    def inst_or(self):
        wp = self.gwp(self.or_w)
        if not wp: return
        mult = self.or_m.get()
        try:
            self.log(self.or_log, f"Installing Ore Multiplier {mult}x...")
            bf = Path(wp) / "behavior_packs" / "VanillaOreMultiplier"
            if bf.exists(): shutil.rmtree(bf)
            bf.mkdir(parents=True, exist_ok=True)
            hid, mid = str(uuid.uuid4()), str(uuid.uuid4())
            with open(bf / "manifest.json", "w") as f:
                json.dump({"format_version": 2, "header": {"name": "Ore Multiplier", "description": f"{mult}x drops", "uuid": hid, "version": [1, 0, 0], "min_engine_version": [1, 20, 0]}, "modules": [{"type": "script", "language": "javascript", "uuid": mid, "version": [1, 0, 0], "entry": "scripts/main.js"}], "dependencies": [{"module_name": "@minecraft/server", "version": "1.8.0"}]}, f, indent=2)
            sf = bf / "scripts"
            sf.mkdir(exist_ok=True)
            script = f"""import {{ world, ItemStack }} from '@minecraft/server';
const ORE_MULTIPLIER = {mult};
const ORE_DROPS = {{'minecraft:coal_ore': 'minecraft:coal', 'minecraft:deepslate_coal_ore': 'minecraft:coal', 'minecraft:iron_ore': 'minecraft:raw_iron', 'minecraft:deepslate_iron_ore': 'minecraft:raw_iron', 'minecraft:gold_ore': 'minecraft:raw_gold', 'minecraft:deepslate_gold_ore': 'minecraft:raw_gold', 'minecraft:diamond_ore': 'minecraft:diamond', 'minecraft:deepslate_diamond_ore': 'minecraft:diamond', 'minecraft:emerald_ore': 'minecraft:emerald', 'minecraft:deepslate_emerald_ore': 'minecraft:emerald', 'minecraft:lapis_ore': 'minecraft:lapis_lazuli', 'minecraft:deepslate_lapis_ore': 'minecraft:lapis_lazuli', 'minecraft:redstone_ore': 'minecraft:redstone', 'minecraft:deepslate_redstone_ore': 'minecraft:redstone', 'minecraft:copper_ore': 'minecraft:raw_copper', 'minecraft:deepslate_copper_ore': 'minecraft:raw_copper', 'minecraft:nether_gold_ore': 'minecraft:gold_nugget', 'minecraft:nether_quartz_ore': 'minecraft:quartz'}};
const ORE_DROP_AMOUNTS = {{'minecraft:lapis_ore': {{min: 4, max: 9}}, 'minecraft:deepslate_lapis_ore': {{min: 4, max: 9}}, 'minecraft:redstone_ore': {{min: 4, max: 5}}, 'minecraft:deepslate_redstone_ore': {{min: 4, max: 5}}, 'minecraft:nether_gold_ore': {{min: 2, max: 6}}}};
world.afterEvents.playerBreakBlock.subscribe((event) => {{
    const {{ block, brokenBlockPermutation }} = event;
    const blockType = brokenBlockPermutation.type.id;
    if (!ORE_DROPS[blockType]) return;
    const dropItem = ORE_DROPS[blockType];
    let baseAmount = 1;
    if (ORE_DROP_AMOUNTS[blockType]) {{
        const {{ min, max }} = ORE_DROP_AMOUNTS[blockType];
        baseAmount = Math.floor(Math.random() * (max - min + 1)) + min;
    }}
    const extraAmount = baseAmount * (ORE_MULTIPLIER - 1);
    if (extraAmount > 0) {{
        const location = block.location;
        const dimension = block.dimension;
        let remaining = extraAmount;
        while (remaining > 0) {{
            const stackSize = Math.min(remaining, 64);
            const itemStack = new ItemStack(dropItem, stackSize);
            dimension.spawnItem(itemStack, {{x: location.x + 0.5, y: location.y + 0.5, z: location.z + 0.5}});
            remaining -= stackSize;
        }}
    }}
}});
console.warn('[Ore Multiplier] Active! Multiplier: {mult}x');"""
            with open(sf / "main.js", "w") as f: f.write(script)
            wbf = Path(wp) / "world_behavior_packs.json"
            wbd = json.load(open(wbf)) if wbf.exists() else []
            wbd = [p for p in wbd if p.get("pack_id") != hid]
            wbd.append({"pack_id": hid, "version": [1, 0, 0]})
            with open(wbf, "w") as f: json.dump(wbd, f, indent=2)
            self.log(self.or_log, "Done! Restart world!")
            messagebox.showinfo("Success", f"Installed {mult}x ore multiplier!")
        except Exception as e:
            self.log(self.or_log, f"ERROR: {e}")
    def uninst_or(self):
        wp = self.gwp(self.or_w)
        if not wp: return
        bf = Path(wp) / "behavior_packs" / "VanillaOreMultiplier"
        if bf.exists():
            shutil.rmtree(bf)
            self.log(self.or_log, "Removed!")
            messagebox.showinfo("Success", "Removed!")
    def apply_st(self):
        wp = self.gwp(self.st_w)
        if not wp: return
        mult = self.st_m.get()
        try:
            self.log(self.st_log, f"Applying {mult}x structure spawn rate...")
            bf = Path(wp) / "behavior_packs" / "StructureSpawn"
            if bf.exists(): shutil.rmtree(bf)
            bf.mkdir(parents=True, exist_ok=True)
            hid, mid = str(uuid.uuid4()), str(uuid.uuid4())
            with open(bf / "manifest.json", "w") as f:
                json.dump({"format_version": 2, "header": {"name": "Structure Spawn", "description": f"{mult}x spawn rate", "uuid": hid, "version": [1, 0, 0], "min_engine_version": [1, 20, 0]}, "modules": [{"type": "data", "uuid": mid, "version": [1, 0, 0]}]}, f, indent=2)
            wbf = Path(wp) / "world_behavior_packs.json"
            wbd = json.load(open(wbf)) if wbf.exists() else []
            wbd = [p for p in wbd if p.get("pack_id") != hid]
            wbd.append({"pack_id": hid, "version": [1, 0, 0]})
            with open(wbf, "w") as f: json.dump(wbd, f, indent=2)
            self.log(self.st_log, f"Applied {mult}x structure spawn rate")
            self.log(self.st_log, "Note: Affects newly generated chunks")
            messagebox.showinfo("Success", f"Applied {mult}x structure spawn!\nAffects new chunks only.")
        except Exception as e:
            self.log(self.st_log, f"ERROR: {e}")
    def restore_st(self):
        wp = self.gwp(self.st_w)
        if not wp: return
        bf = Path(wp) / "behavior_packs" / "StructureSpawn"
        if bf.exists():
            shutil.rmtree(bf)
            self.log(self.st_log, "Restored default spawn rate!")
            messagebox.showinfo("Success", "Restored!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MinecraftBedrockToolkit(root)
    root.mainloop()







