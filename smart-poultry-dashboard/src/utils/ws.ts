import { WSEvent } from "../types/ws";

type Listener<T> = (event: T) => void;

class WSClient {
  private socket?: WebSocket;
  private listeners: Listener<WSEvent>[] = [];

  connect() {
    if (this.socket) return;

    this.socket = new WebSocket("ws://localhost:8000/ws");

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data) as WSEvent;
      this.listeners.forEach((cb) => cb(data));
    };

    this.socket.onclose = () => {
      this.socket = undefined;
      setTimeout(() => this.connect(), 2000);
    };
  }

  subscribe(cb: Listener<WSEvent>) {
    this.listeners.push(cb);
    return () => {
      this.listeners = this.listeners.filter((l) => l !== cb);
    };
  }
}

export const wsClient = new WSClient();
