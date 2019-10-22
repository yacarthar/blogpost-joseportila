import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ItunesComponent } from './itunes.component';

describe('ItunesComponent', () => {
  let component: ItunesComponent;
  let fixture: ComponentFixture<ItunesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ItunesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ItunesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
