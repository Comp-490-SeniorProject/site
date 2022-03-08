import {Injectable} from "@angular/core"
import {User} from "./user"
import {HttpClient} from "@angular/common/http"

@Injectable({
    providedIn: "root",
})
export class AuthService {
    constructor(private http: HttpClient) {}
    public signIn(userData: User) {
        localStorage.setItem("ACCESS_TOKEN", "access_token")
    }
    public isLoggedIn() {
        return localStorage.getItem("ACCESS_TOKEN") !== null
    }
    public logout() {
        localStorage.removeItem("ACCESS_TOKEN")
    }
    public register(userData: User) {
        userData.username = userData.email
        console.log(userData)
        return this.http.post(
            "http://0.0.0.0:8000/" + "api/accounts/register/",
            userData
        )
    }
}
