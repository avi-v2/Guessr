# Guessr
# 🔇 Guess the Number (No Sound Version)

This is a simplified version of the **Guess the Number** game that runs entirely in the terminal — **no sound effects, no external dependencies**.

✅ Perfect for beginners, classrooms, and systems where `pygame` is not available.

---

## 📌 What's Different in This Version?

| Feature             | Main Branch (`main`) | No Sound Branch (`no_sound`) |
|---------------------|-----------------------|-------------------------------|
| Sound Effects       | ✅ Yes (via `pygame`) | ❌ No                         |
| External Dependencies | `pygame` required    | None                          |
| Cross-platform Ease | Slightly heavier      | ✅ Very lightweight            |

---

## 🎮 Game Overview

- The computer picks a random number between 1 and your chosen upper limit.
- You guess the number until you get it right.
- The game tells you if your guess is too high or too low.
- Keeps track of your attempts.
- Offers replay option after each game.

---

## 💻 How to Run

### Step 1: Clone the Repository and Switch Branch

```bash
git clone https://github.com/your-username/guess-the-number.git
cd guess-the-number
git checkout no_sound
