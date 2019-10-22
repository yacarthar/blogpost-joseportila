import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogGetComponent } from './blog-get.component';

describe('BlogGetComponent', () => {
  let component: BlogGetComponent;
  let fixture: ComponentFixture<BlogGetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BlogGetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BlogGetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
