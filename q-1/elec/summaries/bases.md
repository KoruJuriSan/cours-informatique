# Bases in electricity

## Pages in syllabus

- p1-p16

## Theory

### Current Direction

- Conventional direction: + => -
- Physical direction of electrons: - => +

### Resistors Table

#### Color Hierarchy
| Color   | Unit | Ohms       |
| ------- | ---- | ---------- |
| Silver  | -    | 0.01       |
| Gold    | -    | 0.1        |
| Black   | 0    | 1          |
| Brown   | 1    | 10         |
| Red     | 2    | 100        |
| Orange  | 3    | 1k         |
| Yellow  | 4    | 10k        |
| Green   | 5    | 100k       |
| Blue    | 6    | 1M         |
| Violet  | 7    | 10M        |
| Gray    | 8    | 100M       |
| White   | 9    | 1G         |

#### Tolerance Hierarchy
| Color  | Tolerance |
| ------ | --------- |
| Gray   | ±0.05%    |
| Violet | ±0.1%     |
| Blue   | ±0.25%    |
| Green  | ±0.5%     |
| Brown  | ±1%       |
| Red    | ±2%       |
| Gold   | ±5%       |
| Silver | ±10%      |

> Not really important to study

### Circuit

- Node: Intersection of arrival and exit in a circuit.

- Branch: Portion of the circuit between two nodes.

- Mesh: A path that allows you to go from the beginning to the end of the circuit (often multiple per circuit).

### Battery

- Battery: DC generator

### Resistors

- `_|‾|_|‾|`: Purely calorific resistor (heat)
- `_/\/\/\_` or `-▭-`: Normal resistor

- Decade: Resistance values between a multiple of 1 and 10 (e.g., $1\Omega$-$10\Omega$, $1\Omega$-$10k\Omega$)

- Series: Number of values in a decade, with a rank of ($E_n => \sqrt[n]{10^n}$)

- Rank: $E_n$ (n can have values: 3,6,12,24,48,96)

#### What Can Be a Resistor?
- [x] Physical property
- [x] A receptor
- [x] A mathematical model

### Measurement

- Ammeter, always in series
```
---(A)---
```

> Ideally $R_A$ = 0

- Voltmeter, always in parallel
```
   (V)
  /   \
---------
```

> Ideally $R_V$ = Infinite

- Ohmmeter, always in parallel, open circuit
```
   (O)
  /   \
---▭---
```

#### Amperemetre + Voltmetre = Ohmmetre

##### Montage en Amont (V + A)
- Pour des **petites** resistances (plus precis)
```
       (V)
      /   \
-(A)---▭----
```

##### Montage en Aval (V + A)
- Pour des **grandes** resistances (plus precis)
```
   (V)_____
  /        \
---(A)--▭---
```

#### Large vs Small Resistance
- If $R_{measure} < R_{calculate} =$ Better Downstream
- If $R_{measure} > R_{calculate} =$ Better Upstream

### Generator vs Receptor Conventions

- Generator convention: receptors go in the direction of the current, their values (U) are positive.

- Receptor convention: receptors go in the opposite direction of the current, their values (U) are negative.

### Receptors in Series

#### Intensity
- $I_n$ is equal at every point to $I_{total}$ 

#### Voltage
- The voltages of the receptors add up. $U_{total} = U_1 + U_n...$

> Pay attention to the direction of the currents! (subtraction instead of addition if in the opposite direction)

#### Resistance
- Resistances add up. $R_{eq} = R_1 + R_n...$

### Receptors in Parallel

#### Intensity
- Intensities add up. $I_{total} = I_1 + I_n...$

> Law of nodes

#### Voltage
- $U_n$ is equal at every point to $U_{total}$ 

#### Resistance |!|
- $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_n}...$

### Units

- Potential/Tension/Volts (V, U): Concentration of charges.

- Current/Amperage/Intensity (A, I): The intensity of the electric current in relation to the charge per second.

- Resistance/Ohm ($\Omega$, R): Material's ability to resist the passage of current.

- Power/Watt (W, P): Link between A and I.

- Charge/Coulomb (Q): Electric charge.

- Potential difference (E): Difference in potential between two ends.

## Laws

### Potential Difference in a Battery ("pile" in french)

- $U_{PN} = V_P - V_N$

- $U_{PN}$ = Potential difference (E)
- $V_P$ = Lack of electrons
- $V_N$ = Excess of electrons

> VPN => VP - VN

### Voltage / Power / Charge

- $U = W / Q$

### Ampere / Charge / Time

- $I = Q / t$
- $t$ = time in seconds

### Resistance of a Wire

- $R = \cfrac{raw \times l}{S}$
- $raw$ = Resistance coefficient of a material
- $l$ = length of the wire
- $S$ = surface area of the wire

### Mathiessen

- $R_T = R_0 \times (1+a \times T)$
- $R_T$ = Resistance in relation to temperature
- $R_0$ = Original resistance
- $a$ = Temperature coefficient of a material
- $T$ = Temperature

### Ohm's Law

- $U = R \times I$

### Power Law

- $P = U \times I$

### Joule Effect

- Applies if the receiver is purely calorific
- $W_{cal} = R \times I^2 \times t$
- $t$ = time in seconds

### Law of Nodes

- The sum of incoming currents into the node == the sum of currents leaving the node.

### Law of Meshes

- In a mesh, the sum of voltages (U) is == 0

> Receptor Convention

### Kennelly's Theorem

- Allows switching from a star circuit to a triangle circuit (and vice versa).

![1705828037062](image/bases/1705828037062.png)

- $R_a = \frac{R_1 \times R_2}{R_1 + R_2 + R_3}$ 

- $R_b = \frac{R_2 \times R_3}{R_1 + R_2 + R_3}$ 

- $R_c = \frac{R_1 \times R_3}{R_1 + R_2 + R_3}$

> The denominator is always the same!

> The numerator is always the multiplication of the branches that touch point X' (X=letter)