# Computer Architecture

Before diving into the system design process, it is paramount to understand the building blocks of a computer, their importance, and the role they play in designing systems.

## Components

### Disk

- **Primary storage device** in a computer.
- **Persistent storage**: Data is retained regardless of the machine's power state.
- Modern computers often store **terabytes (TB)** of data on disks.
- **Unit breakdown**:
  - 1 byte = 8 bits (smallest unit in computing).
  - 1 TB = $10^{12}$ bytes (1 trillion bytes).
  - 1 GB = $10^9$ bytes (1 billion bytes).

#### Types of Disks

- **HDD (Hard Disk Drive)**:
  - Mechanical with a read/write head.
  - Slows down over time due to wear and tear.
- **SSD (Solid-State Drive)**:
  - Faster than HDD.
  - No moving parts; relies on electronic data storage.
  - More expensive than HDD.

### RAM (Random Access Memory)

- **Temporary memory** for storing active data and applications.
- Typically smaller in size (1GB - 128GB) but much faster than disks.
- **Volatile memory**: Data is erased when the computer is shut down.
- **Speed Comparison**:
  - Writing 1 MB to RAM: Microseconds ($10^{-6}$ seconds).
  - Writing 1 MB to Disk: Milliseconds ($10^{-3}$ seconds).
- **Usage**:
  - Stores variables and active applications.
  - Works in tandem with the CPU for data transfer but does not directly communicate with the disk.

### CPU (Central Processing Unit)

- Acts as the **brain of the computer**, interfacing between RAM and the disk.
- Executes instructions stored in RAM.
- Performs computations (e.g., addition, subtraction) in milliseconds.
- **Instruction Cycle**:
  1. Fetch instructions from RAM.
  2. Decode instructions.
  3. Execute instructions.
- **Cache**:
  - Extremely fast memory on the CPU die.
  - Reduces latency by storing frequently accessed data.

### Caches

- **Hierarchical Structure**:
  - L1, L2, L3 caches (fast but small in size, KBs to MBs).
- **Read Operations**:
  - Data is first checked in the cache before RAM or disk.
  - Cache is faster because it uses **SRAM** (Static RAM).
- **Applications Beyond Architecture**:
  - Web browsers cache HTML, CSS, JavaScript, etc., for faster page loads.
- **Importance**:
  - Critical for high-speed data access in both hardware and software contexts.

### Moore's Law

- Observation that the number of transistors in CPUs doubles every two years.
- Results in:
  - Increased speed.
  - Reduced cost of computers.
- Recent years have shown a **plateau** in the growth of transistor density.

## More about memory

A computer has a **primary** and **secondary** memory. Primary memory is RAM and secondary memory can be SSD, Hybrid drives or HDD.

These permanent drives are non-volatile.

### Magnetic Hard Drive / Hard Disk Drive (HDD)

- sealed case that has magnetic disks.
- These disks rotate at high speeds and the actual arm writes or reads data.
- These rotate at very high speeds.

### SSD (Solid state drive)

- No moving parts
- Use flash memory chips to store data.
- Very fast, quiet and more energy efficient.
- More resistant to physical shocks.
- More expensive.

### SSHD (Solid State Hybrid Drive)

- Use both.
- Magnetic disks are used to store data and flash memory is used for cache.
- Automatic, firmware decides where data will go.
