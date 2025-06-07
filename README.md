# 🎧 PlayItWithPython

This is a simple collection of Python scripts that demonstrate how to play MP3 and WAV audio files using the [`playsound`](https://pypi.org/project/playsound/) library. It includes basic playback, looped playback, and delayed playback.

---

## 📁 Project Structure

```

PlayItWithPython/
├── play\_single.py           # Plays a single MP3 file
├── play\_loop\_input.py       # Plays a sound multiple times (user input)
├── play\_with\_delay.py       # Plays a sound with delay between plays
├── requirements.txt         # Required libraries
└── README.md

````

---

## 🚀 How to Run

1. **Install the required library:**
```bash
pip install -r requirements.txt
````

2. **Run any script:**

```bash
python play_single.py
```

Make sure to place the audio file (`.mp3` or `.wav`) in the same directory or provide the correct file path.

---

## 🔊 Script Details

### 1. `play_single.py`

Plays a single MP3 file once using `playsound`.

### 2. `play_loop_input.py`

Prompts the user for how many times to play the sound and repeats it that many times.

### 3. `play_with_delay.py`

Plays the sound 3 times with a 2-second delay between each playback using the `time` module.

---

## 📦 Requirements

```txt
playsound
```

Install via:

```bash
pip install playsound
```

---

## ⚠️ Notes

* On **Windows**, `playsound` supports both `.mp3` and `.wav`.
* On **macOS/Linux**, support may vary. `.wav` is generally more reliable.
* If `playsound` doesn't suit your needs, you can explore alternatives like `pygame`, `pydub`, or `simpleaudio`.

---

## 🙌 Credits

Built for Python beginners and interview practice under "Python Interview Questions – Practical Lab Format".

---

Happy Coding & Happy Listening! 🎶

```
