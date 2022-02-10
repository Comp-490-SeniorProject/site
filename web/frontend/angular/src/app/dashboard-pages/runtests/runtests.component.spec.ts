import {ComponentFixture, TestBed} from "@angular/core/testing"

import {RuntestsComponent} from "./runtests.component"

describe("RuntestsComponent", () => {
    let component: RuntestsComponent
    let fixture: ComponentFixture<RuntestsComponent>

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [RuntestsComponent],
        }).compileComponents()
    })

    beforeEach(() => {
        fixture = TestBed.createComponent(RuntestsComponent)
        component = fixture.componentInstance
        fixture.detectChanges()
    })

    it("should create", () => {
        expect(component).toBeTruthy()
    })
})
