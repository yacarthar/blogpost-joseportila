import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Itunes2Component } from './itunes2.component';

describe('Itunes2Component', () => {
  let component: Itunes2Component;
  let fixture: ComponentFixture<Itunes2Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Itunes2Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Itunes2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
