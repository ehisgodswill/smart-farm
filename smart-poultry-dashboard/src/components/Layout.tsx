import Sidebar from "./Sidebar";
import TopNav from "./TopNav";

interface Props {
  children: React.ReactNode;
}

export default function Layout({ children }: Props) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <TopNav />
        <main className="mt-16 p-6 bg-gray-50 min-h-screen">{children}</main>
      </div>
    </div>
  );
}
