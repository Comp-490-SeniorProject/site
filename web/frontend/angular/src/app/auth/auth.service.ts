import {Injectable} from "@angular/core"
import {User} from "./user"
import {HttpClient} from "@angular/common/http"
import {environment} from "src/environments/environment"

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
        return this.http.post(
            environment.baseUrl + "api/accounts/register/",
            userData
        )
    }
}
