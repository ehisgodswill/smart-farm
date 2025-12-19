// import { useEffect, useRef, useState } from "react";

export function useWebSocket(url: string) {
  // const [messages, setMessages] = useState<unknown[]>([]);
  // const ws = useRef<WebSocket | null>(null);

  // useEffect(() => {
  //   ws.current = new WebSocket(url);

  //   ws.current.onmessage = (event) => {
  //     const data = JSON.parse(event.data);
  //     setMessages((prev) => [...prev, data]);
  //   };

  //   ws.current.onclose = () => console.log("WebSocket closed");
  //   ws.current.onerror = (err) => console.error("WS error", err);

  //   // return () => ws.current?.close();
  // }, [url]);

  // return messages;
  return url?[] :[]
}
