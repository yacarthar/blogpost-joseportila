import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CchttpComponent } from './cchttp.component';

describe('CchttpComponent', () => {
  let component: CchttpComponent;
  let fixture: ComponentFixture<CchttpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CchttpComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CchttpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
