# Bloomberg Lite (Electron.js Edition)

A lightweight, open-source reimagining of the Bloomberg Terminal.
Built with modern web technologies, packaged as a cross-platform desktop app.

This project demonstrates **real-time data handling, command-driven UX, and modular dashboards** — inspired by Bloomberg, but designed from scratch as a portfolio project.

---

## ✨ Features (MVP)

* **Command Bar**: type `TICKER <CMD>` to pull market data

  * `AAPL` → show Apple stock price
  * `AAPL <NEWS>` → fetch related headlines
  * `MSFT <CHART 1D>` → display intraday chart

* **Panels (Modular UI)**

  * **Price Panel**: live stock/crypto feed + scrolling ticker tape
  * **Chart Panel**: candlesticks + volume + simple indicators
  * **News Panel**: latest headlines from finance news sources

* **Persistence**

  * Save a **watchlist** of tickers locally (SQLite or IndexedDB)

---

## 🛠️ Tech Stack

### Core

* **[Electron.js](https://www.electronjs.org/)** → cross-platform desktop container

  * Why: replicates Bloomberg’s “always-on desktop tool” feel
* **[React](https://react.dev/)** → UI framework inside Electron renderer

  * Why: component-driven, fast iteration, rich ecosystem
* **[Tailwind CSS](https://tailwindcss.com/)** → utility-first styling

  * Why: quick to build polished Bloomberg-like dark UIs

### Charts & Data Viz

* **[Lightweight Charts](https://tradingview.github.io/lightweight-charts/)** (by TradingView)

  * Why: optimized for financial candlestick charts, free, responsive
* Alt option: **Recharts** for more general graphs

### State Management

* **[Zustand](https://zustand-demo.pmnd.rs/)** or Redux

  * Why: lightweight global store for command parsing → API calls → panel updates

### APIs / Data Sources

* **Markets**: Yahoo Finance, Alpha Vantage, or Finnhub (all free tiers available)
* **News**: NewsAPI, GNews, or RSS feeds (Bloomberg/Reuters where possible)

### Storage

* **SQLite** (via better-sqlite3) for local persistence

  * Why: simple, durable, perfect for small watchlist data
* Alt option: **IndexedDB** (browser-native) if you want no external deps

---

## 📐 Architecture

```
Electron (Main Process)
 ├── Manages app lifecycle, windows
 └── Renderer (React UI)
        ├── Command Bar
        ├── Panels
        │    ├── Price Panel (real-time ticker)
        │    ├── Chart Panel (candlesticks)
        │    └── News Panel (RSS/API)
        └── State Management (Zustand/Redux)
             ├── Parse command input
             ├── Trigger API fetch
             └── Update panels
```

---

## 🚀 Roadmap

* Bootstrap Electron + React + Tailwind skeleton
* Layout panels + command bar (static)
* Hook up market API (Yahoo/Alpha Vantage)
* Display live prices in ticker tape + price panel
* Integrate chart panel with intraday candlestick charts
* Add news panel (RSS / NewsAPI integration)
* Connect with command bar parsing
* Save watchlist (SQLite or IndexedDB)
* Add Bloomberg-like polish (keyboard shortcuts, dark mode, panel resizing)

**Stretch Goals**

* Portfolio tracking (basic P\&L)
* Price alerts (Electron desktop notifications)
* Sentiment analysis on news headlines
* Multi-tabbed workspaces (like Bloomberg’s `<GO>` functions)

---

## 🎯 Why This Tech Stack?

The choices aim to balance **realism, performance, and interview relevance**:

* **Electron** → Bloomberg is a *desktop-first* app; this matches their UX philosophy.
* **React + Tailwind** → fastest way to build modular, Bloomberg-like UIs.
* **TradingView Lightweight Charts** → battle-tested in fintech for candlesticks.
* **Zustand/Redux** → lightweight state manager to drive command parsing.
* **SQLite** → durable local persistence without complexity.
* **Public APIs** → avoid vendor lock-in, keep project easy to run.

---
