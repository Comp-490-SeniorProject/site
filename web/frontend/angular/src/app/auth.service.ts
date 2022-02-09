import {HttpClient} from "@angular/common/http"
import {Injectable} from "@angular/core"
import {BehaviorSubject, Subject} from "rxjs"
import {environment} from "../environments/environment"
import {User} from "./user"

export interface AuthResponse {
    access_token: string
}

@Injectable({
    providedIn: "root",
})
export class AuthService {
    stateChanges: Subject<boolean>

    constructor(private http: HttpClient) {
        this.stateChanges = new BehaviorSubject(this.isLoggedIn())
    }

    public async signIn(userData: User) {
        const response = await this.http
            .post<AuthResponse>(`${environment.serverURL}/sign-in`, userData)
            .toPromise()

        if (!response?.access_token) {
            throw new Error("Invalid response body!")
        }

        localStorage.setItem("ACCESS_TOKEN", response.access_token)
        this.stateChanges.next(true)
    }

    public async register(userData: User) {
        const response = await this.http
            .post<AuthResponse>(`${environment.serverURL}/register`, userData)
            .toPromise()

        if (!response?.access_token) {
            throw new Error("Invalid response body!")
        }

        localStorage.setItem("ACCESS_TOKEN", response.access_token)
        this.stateChanges.next(true)
    }

    public isLoggedIn() {
        return localStorage.getItem("ACCESS_TOKEN") !== null
    }

    public logout() {
        localStorage.removeItem("ACCESS_TOKEN")
    }
}
