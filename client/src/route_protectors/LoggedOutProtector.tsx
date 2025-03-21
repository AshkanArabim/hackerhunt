import { useAppSelector } from "@/store/hooks";
import { Navigate, Outlet } from "react-router-dom";

export default function LoggedOutProtector() {
	const loggedIn: boolean = useAppSelector((state) => state.user.loggedIn) ?? false;

	if (loggedIn) {
		return <Navigate to={"/dashboard"} />;
	}

	return <Outlet />;
}
